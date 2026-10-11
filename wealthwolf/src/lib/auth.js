import { useEffect, useState, useSyncExternalStore } from 'react'
import { configured, supabase, supabaseKey, supabaseUrl } from './supabase.js'

// Who's signed in, as a small external store like the progress store:
//   loading  Supabase is still restoring a saved session, or finishing a
//            Google sign-in from the URL (don't redirect yet)
//   guest    nobody signed in
//   user     signed in; `user` holds the profile
let snapshot = { status: configured ? 'loading' : 'guest', user: null }
const listeners = new Set()

function profileOf(user) {
  const meta = user.user_metadata ?? {}
  return {
    uid: user.id,
    name: meta.full_name || meta.name || '',
    email: user.email || '',
    photoURL: meta.avatar_url || meta.picture || '',
  }
}

function publish(session) {
  snapshot = session?.user ? { status: 'user', user: profileOf(session.user) } : { status: 'guest', user: null }
  for (const listener of listeners) listener()
}

// Fires once on load (INITIAL_SESSION), then on every sign-in, sign-out and refresh.
if (supabase) supabase.auth.onAuthStateChange((_event, session) => publish(session))

function subscribe(listener) {
  listeners.add(listener)
  return () => listeners.delete(listener)
}

export function getAuthState() {
  return snapshot
}

export function useAuth() {
  return useSyncExternalStore(subscribe, getAuthState)
}

// Which sign-in methods are switched on in the Supabase dashboard. Read from
// the project's public settings, so the Google button never sends anyone to
// an error page when Google isn't set up.
let settingsRequest = null
export function getAuthSettings() {
  if (!configured) return Promise.resolve(null)
  settingsRequest ??= fetch(`${supabaseUrl}/auth/v1/settings`, { headers: { apikey: supabaseKey } })
    .then((response) => (response.ok ? response.json() : Promise.reject(response.status)))
    .then((s) => ({ google: Boolean(s.external?.google), email: Boolean(s.external?.email), confirmEmail: !s.mailer_autoconfirm }))
    .catch(() => {
      settingsRequest = null
      return null
    })
  return settingsRequest
}

export function useAuthSettings() {
  const [settings, setSettings] = useState(null)
  useEffect(() => {
    let live = true
    getAuthSettings().then((s) => live && setSettings(s))
    return () => {
      live = false
    }
  }, [])
  return settings
}

const fail = (code) => Object.assign(new Error(code), { code })

function client() {
  if (!supabase) throw fail('not_configured')
  return supabase
}

const absolute = (path) => new URL(path, window.location.origin).href

// Leaves the page for Google, then comes back to `returnTo` signed in.
export async function signInWithGoogle(returnTo) {
  const { error } = await client().auth.signInWithOAuth({
    provider: 'google',
    options: { redirectTo: absolute(returnTo), queryParams: { prompt: 'select_account' } },
  })
  if (error) throw error
}

// Resolves { needsConfirmation } when the project makes new users confirm their email first.
export async function signUpWithEmail(name, email, password, returnTo) {
  const { data, error } = await client().auth.signUp({
    email: email.trim(),
    password,
    options: { data: { full_name: name.trim() }, emailRedirectTo: absolute(returnTo) },
  })
  if (error) throw error
  // An address that's already registered comes back as a user with no identities.
  if (data.user && data.user.identities?.length === 0) throw fail('user_already_exists')
  return { needsConfirmation: !data.session }
}

export async function signInWithEmail(email, password) {
  const { error } = await client().auth.signInWithPassword({ email: email.trim(), password })
  if (error) throw error
}

export async function sendReset(email) {
  const { error } = await client().auth.resetPasswordForEmail(email.trim(), { redirectTo: absolute('/reset-password') })
  if (error) throw error
}

export async function updatePassword(password) {
  const { error } = await client().auth.updateUser({ password })
  if (error) throw error
}

// Signs out this browser only; other devices stay signed in.
export async function signOut() {
  const { error } = await client().auth.signOut({ scope: 'local' })
  if (error) throw error
}

// An error Supabase sent back in the URL after a Google sign-in, if any.
export function redirectError() {
  const params = new URLSearchParams(window.location.search)
  const hash = new URLSearchParams(window.location.hash.slice(1))
  const code = params.get('error_code') || hash.get('error_code') || params.get('error') || hash.get('error')
  return code ? { code, message: params.get('error_description') || hash.get('error_description') } : null
}

// Supabase error codes, in words a person can act on. null means say nothing.
const MESSAGES = {
  invalid_credentials: 'That email and password don’t match.',
  user_already_exists: 'There’s already an account with that email. Sign in instead.',
  email_exists: 'There’s already an account with that email. Sign in instead.',
  weak_password: 'Use at least 6 characters for your password.',
  email_not_confirmed: 'Confirm your email first. Check your inbox for the link we sent.',
  email_address_invalid: 'That email address doesn’t look right.',
  validation_failed: 'That email address doesn’t look right.',
  missing_email: 'Enter your email address.',
  missing_password: 'Enter a password.',
  same_password: 'That’s your current password. Pick a new one.',
  over_email_send_rate_limit: 'Too many emails sent. Wait a few minutes, then try again.',
  over_request_rate_limit: 'Too many tries. Wait a minute, then try again.',
  provider_disabled: 'Google sign-in isn’t switched on yet.',
  access_denied: null, // they closed or cancelled the Google window
  signup_disabled: 'New sign-ups are switched off right now.',
  not_configured: 'Sign-in isn’t set up yet.',
}

export function friendlyError(error) {
  if (error?.name === 'AuthRetryableFetchError' || error?.status === 0 || error instanceof TypeError) {
    return 'Can’t reach the sign-in service. Check your connection and try again.'
  }
  const code = error?.code
  return code in MESSAGES ? MESSAGES[code] : 'Something went wrong. Try again.'
}
