import { useSyncExternalStore } from 'react'
import { supabase } from './supabase.js'
import { getAuthState, signOut } from './auth.js'
import { applyRemote, getOwner, onLocalChange, progressSnapshot, setOwner, signOutReset } from '../store/store.js'

// Keeps a signed-in player's progress in their account (Supabase table
// public.progress, one row per player), so it follows them to any device. The local store stays the thing the app
// reads; this module copies it up after changes and down when the account's
// copy changes elsewhere.

const SAVE_DELAY = 800
const UNSAVED_KEY = 'wealthwolf:unsaved' // set while a local change hasn't reached the account

// ---- Status, for the account menu ---------------------------------------
//   idle  not signed in · connecting  waiting for the account's copy
//   saving · saved · offline · error
let status = 'idle'
const listeners = new Set()

function setStatus(next) {
  if (next === status) return
  status = next
  for (const listener of listeners) listener()
}

export function useSyncStatus() {
  return useSyncExternalStore(
    (listener) => {
      listeners.add(listener)
      return () => listeners.delete(listener)
    },
    () => status,
  )
}

function markUnsaved(on) {
  try {
    if (on) localStorage.setItem(UNSAVED_KEY, '1')
    else localStorage.removeItem(UNSAVED_KEY)
  } catch {
    // Storage blocked: worst case a change made just before closing the tab is lost.
  }
}

function isUnsaved() {
  try {
    return localStorage.getItem(UNSAVED_KEY) === '1'
  } catch {
    return false
  }
}

// ---- Where the account's copy lives ---------------------------------------
// `watch` reports the account's row (or null for a new account) when sync starts,
// and again whenever the tab comes back into view, so changes made on another
// device show up here. `save` writes the whole row.

function accountRemote(uid) {
  const table = () => supabase.from('progress')
  return {
    watch(onData, onError) {
      let stopped = false
      const load = async () => {
        const { data, error } = await table().select('progress, rev').eq('user_id', uid).maybeSingle()
        if (stopped) return
        if (error) onError(error)
        else onData(data)
      }
      load()
      const onVisible = () => document.visibilityState === 'visible' && load()
      document.addEventListener('visibilitychange', onVisible)
      return () => {
        stopped = true
        document.removeEventListener('visibilitychange', onVisible)
      }
    },
    async save(data) {
      const { error } = await table().upsert({ user_id: uid, ...data, updated_at: new Date().toISOString() })
      if (error) throw error
    },
  }
}

// ---- The sync loop --------------------------------------------------------

let flushNow = null

export function startSync(uid) {
  const remote = accountRemote(uid)
  let ready = false
  let lastRev = null
  let timer = null
  let saving = false
  setStatus('connecting')

  async function save() {
    clearTimeout(timer)
    timer = null
    const rev = crypto.randomUUID()
    lastRev = rev
    setStatus(navigator.onLine === false ? 'offline' : 'saving')
    const { user } = getAuthState()
    saving = true
    try {
      await remote.save({
        progress: progressSnapshot(),
        profile: { name: user?.name ?? '', email: user?.email ?? '', photoURL: user?.photoURL ?? '' },
        rev,
      })
      if (lastRev === rev) {
        markUnsaved(false)
        setStatus('saved')
      }
    } catch {
      setStatus('error')
    } finally {
      saving = false
    }
  }

  function schedule() {
    markUnsaved(true)
    if (!ready) return
    setStatus(navigator.onLine === false ? 'offline' : 'saving')
    clearTimeout(timer)
    timer = setTimeout(save, SAVE_DELAY)
  }

  // The first answer from the account decides whose progress wins.
  function first(data) {
    ready = true
    const owner = getOwner()
    const mine = owner === uid
    if (owner && !mine) applyRemote(null) // another player's leftovers: never upload those
    setOwner(uid)

    // A new account keeps what's on this device (a guest's lesson one).
    if (!data) return save()
    // Changes from this device that never reached the account, or a guest
    // who has got further than the account has: the local copy wins.
    const localXp = progressSnapshot().xp
    if ((mine && isUnsaved()) || (!owner && localXp > (data.progress?.xp ?? 0))) return save()

    lastRev = data.rev
    applyRemote(data.progress)
    markUnsaved(false)
    setStatus('saved')
  }

  const stopWatch = remote.watch(
    (data) => {
      if (!ready) return first(data)
      // Never let a fetch overwrite changes from this device that are still on their way.
      if (!data || data.rev === lastRev || timer || saving || isUnsaved()) return
      // Changed on another device: theirs is newer.
      lastRev = data.rev
      clearTimeout(timer)
      timer = null
      applyRemote(data.progress)
      markUnsaved(false)
      setStatus('saved')
    },
    () => setStatus(navigator.onLine === false ? 'offline' : 'error'),
  )

  const stopLocal = onLocalChange(schedule)
  const onHide = () => timer && save()
  const onOnline = () => isUnsaved() && ready && save()
  const onOffline = () => setStatus('offline')
  window.addEventListener('pagehide', onHide)
  window.addEventListener('online', onOnline)
  window.addEventListener('offline', onOffline)
  flushNow = () => (timer ? save() : Promise.resolve())

  return () => {
    stopWatch()
    stopLocal()
    clearTimeout(timer)
    window.removeEventListener('pagehide', onHide)
    window.removeEventListener('online', onOnline)
    window.removeEventListener('offline', onOffline)
    flushNow = null
    setStatus('idle')
  }
}

// Save anything waiting, sign out, and leave a fresh guest book on this device.
export async function signOutAndReset() {
  const flushed = flushNow?.() ?? Promise.resolve()
  await Promise.race([flushed, new Promise((resolve) => setTimeout(resolve, 3000))])
  await signOut()
  markUnsaved(false)
  signOutReset()
}
