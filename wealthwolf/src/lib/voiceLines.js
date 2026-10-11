// Which lines the Wolf speaks, and how they're read aloud. Pure JS so both the
// app and the Node voice scripts (scripts/voice-*.mjs) can use it.

export const PRAISE = ['Sharp.', 'Clean.', "That's the one.", 'Nailed it.', 'Exactly.', 'Pack-leader energy.', 'Correct. Obviously.']
export const MISS = ['Not quite.', 'Missed it.', 'Close, but no.', 'Nope.']
export const STRIKES = ['Strike 1.', 'Strike 2.', 'Third strike.']

// The title on the feedback band after checking an answer.
export function feedbackTitle({ correct, mode, mistakes, strikes, seed }) {
  if (correct) return PRAISE[seed % PRAISE.length]
  if (mode === 'boss') return mistakes >= strikes ? 'Third strike.' : `Strike ${mistakes}.`
  return MISS[seed % MISS.length]
}

const slug = (text) =>
  text
    .toLowerCase()
    .replace(/[^a-z0-9]+/g, '-')
    .replace(/^-|-$/g, '')

export const barkKey = (title) => `bark-${slug(title)}`

// Strip content markup and swap symbols for the words a narrator would say.
export function speakable(text) {
  return text
    .replace(/\[\[([^\]|]+)(?:\|[^\]]+)?\]\]/g, '$1')
    .replace(/\*\*(.+?)\*\*/g, '$1')
    .replace(/401\(k\)/g, '401k')
    .replace(/\bkWh\b/g, 'kilowatt hours')
    .replace(/\s*×\s*/g, ' times ')
    .replace(/\s*÷\s*/g, ' divided by ')
    .replace(/\s+\+\s+/g, ' plus ')
    .replace(/\s*=\s*/g, ' equals ')
    .replace(/\s*→\s*/g, ', then ')
    .replace(/(^|\s)−\s?(?=\$|\d)/g, '$1minus ')
    .replace(/\s+−\s+/g, ' minus ')
    .replace(/\s*·\s*/g, ', ')
    .replace(/\n\n+/g, ' ')
    .replace(/\s+/g, ' ')
    .trim()
}

// FNV-1a, so a changed line shows up as a stale clip.
export function hash(text) {
  let h = 0x811c9dc5
  for (let i = 0; i < text.length; i++) {
    h ^= text.charCodeAt(i)
    h = Math.imul(h, 0x01000193)
  }
  return (h >>> 0).toString(16).padStart(8, '0')
}

// Every spoken line for the given modules: concept cards, stories and the
// Wolf's speech bubbles. Keys are step ids (a story uses `<lessonId>-story`).
export function voiceLinesFor(modules) {
  const lines = []
  for (const mod of modules) {
    for (const lesson of mod.lessons) {
      if (lesson.story) {
        lines.push({ key: `${lesson.id}-story`, text: speakable(`${lesson.story.title} ${lesson.story.body}`) })
      }
      for (const step of lesson.steps) {
        if (step.type === 'info') lines.push({ key: step.id, text: speakable(`${step.title}. ${step.body}`) })
        else if (step.context) lines.push({ key: step.id, text: speakable(step.context) })
      }
    }
  }
  return lines.map((line) => ({ ...line, hash: hash(line.text) }))
}

export function barkLines() {
  return [...PRAISE, ...MISS, ...STRIKES].map((title) => {
    const text = title
    return { key: barkKey(title), text, hash: hash(text) }
  })
}
