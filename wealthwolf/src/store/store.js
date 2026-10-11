import { useSyncExternalStore } from 'react'
import { dayKey, daysBetween } from '../lib/dates.js'
import { rankForXp } from '../lib/ranks.js'
import { nextStat } from '../lib/srs.js'

const STORAGE_KEY = 'wealthwolf:state'
// Whose progress the local copy is: a Firebase uid, or absent for a guest.
const OWNER_KEY = 'wealthwolf:owner'
const SCHEMA_VERSION = 4
export const MAX_HEARTS = 5
const REPLAY_XP_FACTOR = 0.5
export const PERFECT_BONUS = 5

const TYPE_XP_LABEL = { lesson: 'Lesson', review: 'Review', boss: 'Den Trial', sim: 'Simulator' }

// First clear pays full XP; practising a finished lesson pays half.
export function xpReward(lesson, alreadyCompleted) {
  return alreadyCompleted ? Math.round(lesson.xp * REPLAY_XP_FACTOR) : lesson.xp
}

function initialState() {
  return {
    version: SCHEMA_VERSION,
    startedAt: null,
    xp: 0,
    hearts: MAX_HEARTS,
    streak: { count: 0, lastActiveDay: null },
    // lessonId -> { firstCompletedAt, lastCompletedAt, timesCompleted }
    completed: {},
    // stepId -> { box, seen, wrong, lastSeen } for spaced repetition
    stats: {},
    // termId -> day the learner first met it
    terms: {},
    // termId -> { box, seen, wrong, lastSeen } from word drills in the glossary
    wordStats: {},
    settings: { sound: true, theme: 'light' },
  }
}

// Bump SCHEMA_VERSION and add a step here whenever the persisted shape changes.
const MIGRATIONS = {
  1: (s) => ({ ...s, version: 2, stats: {}, settings: { sound: true } }),
  2: (s) => ({ ...s, version: 3, terms: {} }),
  3: (s) => ({ ...s, version: 4, wordStats: {} }),
}

function migrate(saved) {
  if (!saved || typeof saved !== 'object' || !Number.isInteger(saved.version)) return initialState()
  let s = saved
  while (s.version < SCHEMA_VERSION) {
    const step = MIGRATIONS[s.version]
    if (!step) return initialState()
    s = step(s)
  }
  return s.version === SCHEMA_VERSION ? { ...initialState(), ...s } : initialState()
}

function load() {
  try {
    const raw = localStorage.getItem(STORAGE_KEY)
    return raw ? migrate(JSON.parse(raw)) : initialState()
  } catch {
    return initialState()
  }
}

function persist() {
  try {
    localStorage.setItem(STORAGE_KEY, JSON.stringify(state))
  } catch {
    // Storage full or blocked (private mode): keep playing in memory.
  }
}

let state = load()
const listeners = new Set()
const localChangeListeners = new Set()

function emit() {
  for (const listener of listeners) listener()
}

function setState(update) {
  const next = update(state)
  if (next === state) return
  state = next
  persist()
  emit()
  for (const listener of localChangeListeners) listener()
}

// ---- Account sync hooks (used by lib/sync.js; the store itself knows nothing about Firebase).

// Called after every change the player makes, not after remote data is applied.
export function onLocalChange(listener) {
  localChangeListeners.add(listener)
  return () => localChangeListeners.delete(listener)
}

// Progress without device settings (theme, sound), for saving to an account.
export function progressSnapshot() {
  const progress = { ...state }
  delete progress.settings
  return progress
}

// Replace progress with the account's copy, keeping this device's settings.
export function applyRemote(progress) {
  state = { ...migrate(progress), settings: state.settings }
  persist()
  emit()
}

// Signing out leaves a fresh guest book behind (theme and sound stay).
export function signOutReset() {
  state = { ...initialState(), settings: state.settings }
  setOwner(null)
  persist()
  emit()
}

export function getOwner() {
  try {
    return localStorage.getItem(OWNER_KEY)
  } catch {
    return null
  }
}

export function setOwner(uid) {
  try {
    if (uid) localStorage.setItem(OWNER_KEY, uid)
    else localStorage.removeItem(OWNER_KEY)
  } catch {
    // Storage blocked: the account copy is still the source of truth.
  }
}

function subscribe(listener) {
  listeners.add(listener)
  return () => listeners.delete(listener)
}

// Keep tabs in sync: progress made in one tab shows up in the others.
window.addEventListener('storage', (event) => {
  if (event.key !== STORAGE_KEY) return
  state = load()
  emit()
})

export function getState() {
  return state
}

// Selectors must return primitives or existing references (not new objects),
// or React will re-render forever. Derive objects in the component instead.
export function useStore(selector = (s) => s) {
  return useSyncExternalStore(subscribe, () => selector(state))
}

// A streak survives until the end of the day after the last lesson.
export function liveStreak(streak, today = dayKey()) {
  if (!streak.lastActiveDay) return 0
  return daysBetween(streak.lastActiveDay, today) <= 1 ? streak.count : 0
}

export const actions = {
  startLearning() {
    setState((s) => (s.startedAt ? s : { ...s, startedAt: new Date().toISOString() }))
  },

  // Returns what happened so the lesson screen can celebrate it.
  // `skipped` marks a node done without paying XP (used while the simulator is unbuilt).
  completeLesson(lesson, { perfect = false, skipped = false } = {}) {
    const before = state
    const today = dayKey()
    const prior = before.completed[lesson.id]
    const breakdown = []
    const kind = lesson.scope === 'section' ? 'Section Trial' : TYPE_XP_LABEL[lesson.type] ?? 'Lesson'
    if (!skipped) breakdown.push({ label: prior ? 'Practice' : kind, xp: xpReward(lesson, Boolean(prior)) })
    if (perfect && !skipped) breakdown.push({ label: 'Perfect', xp: PERFECT_BONUS })
    const xpGained = breakdown.reduce((sum, item) => sum + item.xp, 0)

    const gap = before.streak.lastActiveDay ? daysBetween(before.streak.lastActiveDay, today) : null
    const streakCount = gap === 0 ? before.streak.count : gap === 1 ? before.streak.count + 1 : 1

    const now = new Date().toISOString()
    setState((s) => ({
      ...s,
      startedAt: s.startedAt ?? now,
      xp: s.xp + xpGained,
      streak: { count: streakCount, lastActiveDay: today },
      completed: {
        ...s.completed,
        [lesson.id]: {
          firstCompletedAt: prior?.firstCompletedAt ?? now,
          lastCompletedAt: now,
          timesCompleted: (prior?.timesCompleted ?? 0) + 1,
        },
      },
    }))

    const rankBefore = rankForXp(before.xp).rank
    const rankAfter = rankForXp(state.xp).rank
    return {
      xpGained,
      breakdown,
      xpBefore: before.xp,
      xpAfter: state.xp,
      firstTime: !prior,
      streak: streakCount,
      streakExtended: gap !== 0,
      rankUp: rankAfter.id !== rankBefore.id ? rankAfter : null,
    }
  },

  recordAnswer(stepId, correct) {
    const today = dayKey()
    setState((s) => ({ ...s, stats: { ...s.stats, [stepId]: nextStat(s.stats[stepId], correct, today) } }))
  },

  learnTerms(ids) {
    const fresh = ids.filter((id) => !state.terms[id])
    if (!fresh.length) return
    const today = dayKey()
    setState((s) => ({ ...s, terms: { ...s.terms, ...Object.fromEntries(fresh.map((id) => [id, today])) } }))
  },

  recordWord(termId, correct) {
    const today = dayKey()
    setState((s) => ({ ...s, wordStats: { ...s.wordStats, [termId]: nextStat(s.wordStats[termId], correct, today) } }))
  },

  setSound(on) {
    setState((s) => ({ ...s, settings: { ...s.settings, sound: on } }))
  },

  setTheme(theme) {
    setState((s) => ({ ...s, settings: { ...s.settings, theme } }))
  },

  loseHeart() {
    setState((s) => (s.hearts > 0 ? { ...s, hearts: s.hearts - 1 } : s))
  },

  refillHearts() {
    setState((s) => (s.hearts === MAX_HEARTS ? s : { ...s, hearts: MAX_HEARTS }))
  },

  resetProgress() {
    setState(() => initialState())
  },
}

if (import.meta.env.DEV) window.__wealthwolf = { getState, actions }
