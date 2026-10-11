import { useSyncExternalStore } from 'react'
import {
  GoogleAuthProvider,
  createUserWithEmailAndPassword,
  onAuthStateChanged,
  sendPasswordResetEmail,
  signInWithEmailAndPassword,
  signInWithPopup,
  signInWithRedirect,
  signOut as firebaseSignOut,
  updateProfile,
} from 'firebase/auth'
import { auth, configured } from './firebase.js'

// Who's signed in, as a small external store like the progress store:
//   loading  Firebase is still restoring a saved session (don't redirect yet)
//   guest    nobody signed in
//   user     signed in; `user` holds the profile
let snapshot = { status: configured ? 'loading' : 'guest', user: null }
const listeners = new Set()

function profileOf(user) {
  return {
    uid: user.uid,
    name: user.displayName || '',
    email: user.email || '',
    photoURL: user.photoURL || '',
  }
}

function publish(user) {
  snapshot = user ? { status: 'user', user: profileOf(user) } : { status: 'guest', user: null }
  for (const listener of listeners) listener()
}

if (auth) onAuthStateChanged(auth, publish)

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

function requireAuth() {
  if (!auth) throw Object.assign(new Error('Firebase is not configured'), { code: 'app/not-configured' })
  return auth
}

export async function signInWithGoogle() {
  const a = requireAuth()
  const provider = new GoogleAuthProvider()
  provider.setCustomParameters({ prompt: 'select_account' })
  try {
    await signInWithPopup(a, provider)
  } catch (error) {
    // Some browsers block the popup outright; a full-page redirect still works.
    if (error.code === 'auth/popup-blocked') return signInWithRedirect(a, provider)
    throw error
  }
}

export async function signUpWithEmail(name, email, password) {
  const a = requireAuth()
  const { user } = await createUserWithEmailAndPassword(a, email.trim(), password)
  if (name.trim()) {
    await updateProfile(user, { displayName: name.trim() })
    publish(a.currentUser) // the first auth event fired before the name was set
  }
}

export function signInWithEmail(email, password) {
  return signInWithEmailAndPassword(requireAuth(), email.trim(), password)
}

export function sendReset(email) {
  return sendPasswordResetEmail(requireAuth(), email.trim())
}

export function signOut() {
  return firebaseSignOut(requireAuth())
}

// Firebase error codes, in words a person can act on. null means say nothing
// (they closed the Google window themselves).
const MESSAGES = {
  'auth/email-already-in-use': 'There’s already an account with that email. Sign in instead.',
  'auth/invalid-credential': 'That email and password don’t match.',
  'auth/invalid-login-credentials': 'That email and password don’t match.',
  'auth/wrong-password': 'That email and password don’t match.',
  'auth/user-not-found': 'That email and password don’t match.',
  'auth/invalid-email': 'That email address doesn’t look right.',
  'auth/missing-email': 'Enter your email address.',
  'auth/missing-password': 'Enter a password.',
  'auth/weak-password': 'Use at least 6 characters for your password.',
  'auth/account-exists-with-different-credential': 'That email already has an account. Sign in the way you signed up.',
  'auth/network-request-failed': 'Can’t reach the sign-in service. Check your connection and try again.',
  'auth/too-many-requests': 'Too many tries. Wait a minute, then try again.',
  'auth/operation-not-allowed': 'That way of signing in isn’t switched on in Firebase yet.',
  'auth/unauthorized-domain': 'This address isn’t on the Firebase project’s list of allowed domains.',
  'auth/popup-closed-by-user': null,
  'auth/cancelled-popup-request': null,
  'auth/user-cancelled': null,
  'app/not-configured': 'Sign-in isn’t set up yet.',
}

export function friendlyError(error) {
  const code = error?.code
  return code in MESSAGES ? MESSAGES[code] : 'Something went wrong. Try again.'
}
