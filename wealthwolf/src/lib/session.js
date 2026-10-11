import { gradedSteps, lessons, plain } from './content.js'
import { urgency } from './srs.js'
import { dayKey } from './dates.js'

export const BOSS_STRIKES = 3

export function shuffle(list) {
  const out = [...list]
  for (let i = out.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1))
    ;[out[i], out[j]] = [out[j], out[i]]
  }
  return out
}

const range = (n) => Array.from({ length: n }, (_, i) => i)

// A shuffle that never hands back the original order (when that's possible).
function scramble(n) {
  if (n < 2) return range(n)
  let order
  do order = shuffle(range(n))
  while (order.every((v, i) => v === i))
  return order
}

let nextKey = 0

// Freeze the randomness for one appearance of a step, so re-renders are stable
// and a re-queued question comes back freshly shuffled.
export function present(step) {
  const card = { key: `${step.id}#${nextKey++}`, step }
  if (step.type === 'multiple_choice' || step.type === 'fill_blank') card.order = shuffle(range(step.choices.length))
  if (step.type === 'order') card.order = scramble(step.items.length)
  if (step.type === 'match') {
    card.left = shuffle(range(step.pairs.length))
    card.right = scramble(step.pairs.length)
  }
  if (step.type === 'sort') card.order = shuffle(range(step.items.length))
  return card
}

// What an untouched answer looks like for each step type.
export function initialAnswer(card) {
  switch (card?.step.type) {
    case 'order':
      return []
    case 'allocate':
      return card.step.categories.map((c) => c.fixed ?? 0)
    default:
      return null
  }
}

export function allocated(answer) {
  return Array.isArray(answer) ? answer.reduce((sum, n) => sum + n, 0) : 0
}

// Each budget-builder category is judged on its own rule, not on one exact split.
export function categoryOk(category, amount) {
  if (category.fixed !== undefined) return amount === category.fixed
  if (category.min !== undefined && amount < category.min) return false
  if (category.max !== undefined && amount > category.max) return false
  return true
}

// Pick the questions most in need of review, preferring the given module on ties.
function weakest(steps, count, stats, preferModuleId) {
  const today = dayKey()
  return shuffle(steps)
    .map((step) => ({
      step,
      score: urgency(stats[step.id], today) + (step.moduleId === preferModuleId ? 0.25 : 0),
    }))
    .sort((a, b) => b.score - a.score)
    .slice(0, count)
    .map((entry) => entry.step)
}

// A Section Trial should test the whole section: take the weakest question from
// each unit in turn (in a shuffled order each round) until there are enough.
function acrossUnits(steps, count, stats) {
  const byUnit = new Map()
  for (const step of steps) byUnit.set(step.moduleId, [...(byUnit.get(step.moduleId) ?? []), step])
  const queues = [...byUnit.values()].map((list) => weakest(list, list.length, stats))
  const picked = []
  while (picked.length < count && queues.some((q) => q.length)) {
    for (const queue of shuffle(queues)) if (queue.length && picked.length < count) picked.push(queue.shift())
  }
  return picked
}

function stepsFrom(lessonList) {
  return lessonList.flatMap((l) => gradedSteps(l).map((step) => ({ ...step, moduleId: l.moduleId })))
}

export function buildSession(lesson, { completed, stats }) {
  if (lesson.type === 'review') {
    const pool = stepsFrom(lessons.filter((l) => completed[l.id] && l.type !== 'review'))
    return { mode: 'review', cards: shuffle(weakest(pool, lesson.draw ?? 8, stats, lesson.moduleId)).map(present) }
  }

  if (lesson.type === 'boss') {
    const own = gradedSteps(lesson)
    const ownIds = new Set(own.map((s) => s.id))
    // A unit's trial draws from that unit; a Section Trial from every unit in the section.
    const inScope = lesson.scope === 'section' ? (l) => l.sectionId === lesson.sectionId : (l) => l.moduleId === lesson.moduleId
    const pool = stepsFrom(lessons.filter((l) => inScope(l) && l.type === 'lesson'))
    const candidates = pool.filter((s) => !ownIds.has(s.id))
    const pulled =
      lesson.scope === 'section'
        ? acrossUnits(candidates, lesson.draw ?? 12, stats)
        : weakest(candidates, lesson.draw ?? 3, stats, lesson.moduleId)
    return { mode: 'boss', cards: shuffle([...own, ...pulled]).map(present) }
  }

  const cards = lesson.steps.map(present)
  if (lesson.story) cards.unshift(present({ id: `${lesson.id}-story`, type: 'story', ...lesson.story }))
  return { mode: 'lesson', cards }
}

export function isReady(card, answer) {
  switch (card.step.type) {
    case 'multiple_choice':
    case 'fill_blank':
    case 'true_false':
      return answer !== null && answer !== undefined
    case 'number':
      return parseNumber(answer) !== null
    case 'order':
      return Array.isArray(answer) && answer.length === card.step.items.length
    case 'spot':
      return typeof answer === 'string'
    case 'allocate':
      return allocated(answer) === card.step.total
    default:
      return false
  }
}

export function grade(card, answer) {
  const { step } = card
  switch (step.type) {
    case 'multiple_choice':
    case 'fill_blank':
    case 'true_false':
      return answer === step.answer
    case 'number':
      return Math.abs(parseNumber(answer) - step.answer) <= (step.tolerance ?? 0)
    case 'order':
      return answer.every((itemIndex, position) => itemIndex === position)
    case 'match':
    case 'sort':
      return true // these only finish once every item is right
    case 'spot':
      return answer === step.answer
    case 'allocate':
      return allocated(answer) === step.total && step.categories.every((c, i) => categoryOk(c, answer[i]))
    default:
      return false
  }
}

// What to show in the "correct answer" line after a miss.
export function solutionText(step) {
  switch (step.type) {
    case 'multiple_choice':
    case 'fill_blank':
      return plain(step.choices[step.answer])
    case 'true_false':
      return step.answer ? 'True' : 'False'
    case 'number':
      if (step.unit === '$') return formatMoney(step.answer)
      return formatNumber(step.answer) + (step.unit ? (step.unit === '%' ? '%' : ` ${step.unit}`) : '')
    case 'order':
      return step.items.map(plain).join('  →  ')
    case 'spot':
      return step.doc.lines.find((l) => l.id === step.answer).label
    case 'allocate':
      return [
        ...step.categories
          .filter((c) => c.fixed === undefined && (c.min !== undefined || c.max !== undefined))
          .map((c) =>
            c.min !== undefined && c.max !== undefined
              ? `${c.label} between ${formatMoney(c.min)} and ${formatMoney(c.max)}`
              : c.min !== undefined
                ? `${c.label} at least ${formatMoney(c.min)}`
                : `${c.label} at most ${formatMoney(c.max)}`,
          ),
        'nothing left to assign',
      ].join(' · ')
    default:
      return ''
  }
}

export function parseNumber(raw) {
  if (typeof raw !== 'string') return null
  const cleaned = raw.replace(/[,\s]/g, '').replace(/[−–]/g, '-')
  if (!/^-?\d*\.?\d+$/.test(cleaned)) return null
  return Number(cleaned)
}

export function formatNumber(n) {
  return n.toLocaleString('en-US', { maximumFractionDigits: 2 }).replace('-', '−')
}

// Dollars. Whole amounts stay whole ($300); anything with cents shows both digits ($84.10).
export function formatMoney(n, { cents = !Number.isInteger(n) } = {}) {
  const digits = cents ? 2 : 0
  const body = Math.abs(n).toLocaleString('en-US', { minimumFractionDigits: digits, maximumFractionDigits: digits })
  return `${n < 0 ? '−' : ''}$${body}`
}
