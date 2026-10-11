import { daysBetween } from './dates.js'

// Leitner-style spaced repetition. Every answer moves a question between boxes:
// right moves it up one, wrong drops it to box 1. Higher boxes wait longer
// before they're due again.
export const MAX_BOX = 5
const INTERVAL_DAYS = [0, 0, 1, 3, 7, 14] // indexed by box

export function nextStat(stat, correct, today) {
  const box = correct ? Math.min((stat?.box ?? 0) + 1, MAX_BOX) : 1
  return {
    box,
    seen: (stat?.seen ?? 0) + 1,
    wrong: (stat?.wrong ?? 0) + (correct ? 0 : 1),
    lastSeen: today,
  }
}

// How overdue a question is, in days. Higher means it needs review sooner.
// Never-seen questions rank first.
export function urgency(stat, today) {
  if (!stat?.lastSeen) return Number.POSITIVE_INFINITY
  return daysBetween(stat.lastSeen, today) - INTERVAL_DAYS[stat.box] + (MAX_BOX - stat.box) * 0.5
}
