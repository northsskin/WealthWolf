import { useSyncExternalStore } from 'react'
import { doc, onSnapshot, serverTimestamp, setDoc } from 'firebase/firestore'
import { db } from './firebase.js'
import { getAuthState, signOut } from './auth.js'
import { applyRemote, getOwner, onLocalChange, progressSnapshot, setOwner, signOutReset } from '../store/store.js'

// Keeps a signed-in player's progress in their account (Firestore users/{uid}),
// so it follows them to any device. The local store stays the thing the app
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
// Both remotes call onData(null) for an account with nothing saved yet.

function firestoreRemote(uid) {
  const ref = doc(db, 'users', uid)
  return {
    watch(onData, onError) {
      return onSnapshot(
        ref,
        (snap) => {
          if (snap.metadata.hasPendingWrites) return // our own write, echoed back
          if (!snap.exists() && snap.metadata.fromCache) return // offline: "missing" isn't known yet
          onData(snap.exists() ? snap.data() : null)
        },
        onError,
      )
    },
    save: (data) => setDoc(ref, { ...data, updatedAt: serverTimestamp() }),
  }
}

// Emulator mode has no Firestore (its emulator needs Java), so the account's
// copy is kept in localStorage under its own key. Signing out wipes the
// player's local progress but not this, so restoring on sign-in still works.
function localRemote(uid) {
  const key = `wealthwolf:remote:${uid}`
  const read = () => {
    try {
      return JSON.parse(localStorage.getItem(key))
    } catch {
      return null
    }
  }
  return {
    watch(onData) {
      const timer = setTimeout(() => onData(read()), 150) // a beat, like a network round trip
      const onStorage = (event) => event.key === key && onData(read())
      window.addEventListener('storage', onStorage)
      return () => {
        clearTimeout(timer)
        window.removeEventListener('storage', onStorage)
      }
    },
    save: async (data) => localStorage.setItem(key, JSON.stringify({ ...data, updatedAt: Date.now() })),
  }
}

// ---- The sync loop --------------------------------------------------------

let flushNow = null

export function startSync(uid) {
  const remote = db ? firestoreRemote(uid) : localRemote(uid)
  let ready = false
  let lastRev = null
  let timer = null
  setStatus('connecting')

  async function save() {
    clearTimeout(timer)
    timer = null
    const rev = crypto.randomUUID()
    lastRev = rev
    setStatus(navigator.onLine === false ? 'offline' : 'saving')
    const { user } = getAuthState()
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
      if (!data || data.rev === lastRev) return
      // Changed on another device: theirs is newer.
      lastRev = data.rev
      clearTimeout(timer)
      timer = null
      applyRemote(data.progress)
      markUnsaved(false)
      setStatus('saved')
    },
    () => setStatus('error'),
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
