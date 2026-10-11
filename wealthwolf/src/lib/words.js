import { glossary, modules, termOrigins } from './content.js'
import { present, shuffle } from './session.js'
import { urgency } from './srs.js'

// The glossary's word drill: quick questions on words the learner has already
// met in lessons. Results feed a Leitner box per word, kept apart from the
// lesson questions' stats.

export const DRILL_SIZE = 8
export const MIN_DRILL_WORDS = 4
const SOLID_BOX = 3

// How a learned word is holding up in drills:
//   new         never drilled
//   practising  right so far, not yet enough times to call it solid
//   shaky       missed, and not yet answered right enough times since
//   solid       right in at least three drills in a row
export function wordStatus(stat) {
  if (!stat) return 'new'
  if (stat.box >= SOLID_BOX) return 'solid'
  return stat.wrong > 0 ? 'shaky' : 'practising'
}

export const STATUS_LABEL = { solid: 'Solid', practising: 'Practising', shaky: 'Shaky', new: 'Not drilled yet' }

// Every glossary word in the order the path teaches it.
export const wordsInPathOrder = Object.keys(glossary).sort(
  (a, b) => (termOrigins[a]?.position ?? Infinity) - (termOrigins[b]?.position ?? Infinity),
)

// The unit a word belongs to: where it's taught, or where it's defined if no lesson teaches it yet.
export function wordModule(id) {
  return termOrigins[id]?.moduleId ?? modules.find((m) => m.terms?.[id])?.id
}

export function learnedWords(terms) {
  return wordsInPathOrder.filter((id) => terms[id])
}

// Shaky words first, then ones never drilled (oldest first), then whatever is most overdue.
function drillOrder(ids, wordStats, today) {
  const group = (id) => ({ shaky: 0, new: 1 }[wordStatus(wordStats[id])] ?? 2)
  return [...ids].sort(
    (a, b) =>
      group(a) - group(b) ||
      urgency(wordStats[b], today) - urgency(wordStats[a], today) ||
      (termOrigins[a]?.position ?? 0) - (termOrigins[b]?.position ?? 0),
  )
}

// Wrong answers come from the words you know, nearest first: same unit before others.
function distractors(id, pool, count) {
  const home = wordModule(id)
  const others = shuffle(pool.filter((other) => other !== id))
  return others.sort((a, b) => (wordModule(b) === home) - (wordModule(a) === home)).slice(0, count)
}

// Two ways to ask: show the meaning and pick the word, or show the word and pick its meaning.
function drillStep(id, ask, pool) {
  const entry = glossary[id]
  const explain = entry.example ? `**Example:** ${entry.example}` : undefined
  if (ask === 'word') {
    const options = [id, ...distractors(id, pool, 3)]
    return {
      id: `word-${id}`,
      wordId: id,
      type: 'multiple_choice',
      prompt: 'Which word means this?',
      cue: entry.definition,
      cueKind: 'meaning',
      choices: options.map((o) => glossary[o].term),
      answer: 0,
      explain,
    }
  }
  const options = [id, ...distractors(id, pool, 2)]
  return {
    id: `word-${id}`,
    wordId: id,
    type: 'multiple_choice',
    prompt: 'What does this word mean?',
    cue: entry.term,
    cueKind: 'word',
    choices: options.map((o) => glossary[o].definition),
    answer: 0,
    explain,
  }
}

// A drill session: up to DRILL_SIZE cards, half asked each way.
export function buildDrill(terms, wordStats, today) {
  const pool = learnedWords(terms)
  if (pool.length < MIN_DRILL_WORDS) return []
  const picked = shuffle(drillOrder(pool, wordStats, today).slice(0, DRILL_SIZE))
  return picked.map((id, i) => present(drillStep(id, i % 2 ? 'meaning' : 'word', pool)))
}
