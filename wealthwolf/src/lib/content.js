// Loads the course from src/data/ at build time. The path is split into
// sections (src/data/sections.json, in `order`), each holding units: one JSON
// file per unit in src/data/<section-id>/, placed by its own `order`. To add a
// unit, drop a file in its section's folder.
//
// Section: { id, order, title, description, trial? }   trial = { id, title, summary, xp, draw }:
//          a Den Trial over the whole section, played after its last unit
// Module (unit): { id, section, order, title, description, wolfLine, terms, lessons: Lesson[] }
// Lesson: { id, type, format?, title, summary, xp, steps: Step[], draw?, story? }
//   format  how a 'lesson' plays, shown on the path: concept (default), document,
//           story, spot, sort, call
//   story   { title, character, body } read first; its questions keep it one tap away
//   type 'lesson'  plays its own steps in order
//   type 'review'  plays `draw` questions picked by spaced repetition from finished lessons
//   type 'boss'    plays its own questions plus `draw` from the module (or, for a
//                  Section Trial, from the whole section); three strikes fails it
//   type 'sim'     Portfolio Simulator (not built yet)
//
// Step types (every step has a unique `id`; graded steps take optional `context` and `explain`):
//   info            { title, body, callout? }            body supports \n\n paragraphs
//   multiple_choice { prompt, choices[], answer: index }
//   true_false      { prompt, answer: boolean }
//   fill_blank      { prompt with "___", choices[], answer: index }
//   number          { prompt, answer: number, unit?, tolerance? }
//   order           { prompt, items[] in the correct order }
//   match           { prompt, pairs: [left, right][] }
//   spot            { prompt, doc, answer: lineId }      tap the line on the document
//   sort            { prompt, buckets[], items: [text, bucketIndex][] }
//   allocate        { prompt, total, step, categories: [{ label, fixed?, min?, max? }] }
//
// Any graded step may also carry `doc` (or `docs`, up to two, for comparing):
//   { kind: 'paystub'|'bill'|'receipt'|'statement', title, subtitle?, meta?: [label, value][],
//     lines: [{ id, label, amount, section?, date?, qty? }], totals?: [{ label, amount, strong? }], note? }
// Multiple choice may carry `why[]`: one line per choice, shown when that wrong choice is picked.
// Money number steps use "unit": "$" (shown as a prefix); cents need "tolerance": 0.005.
//
// `context` is a teaching line the wolf says above the question. Text fields
// support **bold** and [[term]] / [[display text|term-id]] glossary links.
// Terms live in each module's `terms` map: { id: { term, definition, example? } }.
// A term is "introduced" by the first step on the path that mentions it in a
// teaching field (title, body, callout, context, prompt), so write that step
// to actually teach it.

import sectionList from '../data/sections.json'

const files = import.meta.glob('../data/*/*.json', { eager: true, import: 'default' })
const sectionOrder = new Map(sectionList.map((section) => [section.id, section.order]))

// Every unit, in path order: by section, then by its place in the section.
export const modules = Object.values(files).sort(
  (a, b) => (sectionOrder.get(a.section) ?? Infinity) - (sectionOrder.get(b.section) ?? Infinity) || a.order - b.order,
)

// Sections that have at least one unit, numbered in path order.
export const sections = [...sectionList]
  .sort((a, b) => a.order - b.order)
  .map((section) => ({ ...section, units: modules.filter((m) => m.section === section.id) }))
  .filter((section) => section.units.length)
  .map((section, i) => ({ ...section, number: i + 1 }))

// Every lesson in path order, tagged with its unit, section and position.
// Steps from a story lesson remember it, so a review question can still show the story.
// A section's trial comes after its last unit.
export const lessons = sections.flatMap((section) => [
  ...section.units.flatMap((mod) =>
    mod.lessons.map((lesson, indexInModule) => ({
      ...lesson,
      format: lesson.format ?? 'concept',
      moduleId: mod.id,
      sectionId: section.id,
      indexInModule,
      steps: lesson.story ? lesson.steps.map((step) => ({ ...step, storyOf: lesson.id })) : lesson.steps,
    })),
  ),
  ...(section.trial
    ? [{ ...section.trial, type: 'boss', scope: 'section', format: 'concept', moduleId: null, sectionId: section.id, indexInModule: 0, steps: [] }]
    : []),
])

const lessonIndex = new Map(lessons.map((l, i) => [l.id, i]))

export const glossary = Object.assign({}, ...modules.map((m) => m.terms ?? {}))

const TERM_LINK = /\[\[([^\]|]+)(?:\|([^\]]+))?\]\]/g

export const termId = (text) =>
  text
    .toLowerCase()
    .replace(/[^a-z0-9]+/g, '-')
    .replace(/^-|-$/g, '')

export function termsIn(text) {
  return typeof text === 'string' ? [...text.matchAll(TERM_LINK)].map((m) => m[2] ?? termId(m[1])) : []
}

// Strip markup for places that can't hold a tappable term, like answer buttons.
export function plain(text) {
  return text.replace(TERM_LINK, '$1').replace(/\*\*(.+?)\*\*/g, '$1')
}

const TEACHING_FIELDS = ['title', 'body', 'callout', 'context', 'prompt']

// Terms a step teaches or uses up front (not ones that only appear in the explanation).
export function stepTerms(step) {
  return [...new Set(TEACHING_FIELDS.flatMap((field) => termsIn(step[field])))]
}

function allText(step) {
  return [
    ...TEACHING_FIELDS.map((f) => step[f]),
    step.explain,
    ...(step.choices ?? []),
    ...(step.why ?? []),
    ...(step.items ?? []).flat(),
    ...(step.pairs ?? []).flat(),
  ].filter((t) => typeof t === 'string')
}

// Where each glossary word is first taught on the path, in path order:
// termId -> { lessonId, moduleId, position }. Mirrors when the player marks it learned.
export const termOrigins = (() => {
  const origins = {}
  const note = (id, lesson) => {
    if (!origins[id] && glossary[id]) {
      origins[id] = { lessonId: lesson.id, moduleId: lesson.moduleId, position: Object.keys(origins).length }
    }
  }
  for (const lesson of lessons) {
    if (lesson.story) termsIn(lesson.story.body).forEach((id) => note(id, lesson))
    for (const step of lesson.steps) stepTerms(step).forEach((id) => note(id, lesson))
  }
  return origins
})()

export function stepDocs(step) {
  return step.docs ?? (step.doc ? [step.doc] : [])
}

export function getLesson(id) {
  const i = lessonIndex.get(id)
  return i === undefined ? null : lessons[i]
}

export function getModule(id) {
  return modules.find((m) => m.id === id) ?? null
}

export const GRADED_TYPES = new Set(['multiple_choice', 'true_false', 'fill_blank', 'number', 'order', 'match', 'spot', 'sort', 'allocate'])

export function gradedSteps(lesson) {
  return lesson.steps.filter((s) => GRADED_TYPES.has(s.type))
}

// Testing switch: VITE_UNLOCK_ALL=1 (set in .env.emu) opens every lesson, account or not.
export const UNLOCK_ALL = import.meta.env.VITE_UNLOCK_ALL === '1'

// Linear unlock: a lesson opens once the one before it on the path is done.
export function lessonStatus(id, completed) {
  if (completed[id]) return 'completed'
  const i = lessonIndex.get(id)
  if (i === undefined) return 'locked'
  if (UNLOCK_ALL || i === 0 || completed[lessons[i - 1].id]) return 'available'
  return 'locked'
}

// Lesson one is free to play without an account; everything after it needs one.
export function canPlay(lesson, signedIn) {
  return UNLOCK_ALL || signedIn || lesson?.id === lessons[0].id
}

// The first lesson the player hasn't finished, or null once everything is done.
export function currentLessonId(completed) {
  return lessons.find((l) => !completed[l.id])?.id ?? null
}

// Content is hand-written JSON, so catch authoring mistakes loudly in dev.
// Returns a list of problems; `npm run check` runs it from the command line.
export function validateContent() {
  const problems = []
  const seen = new Set()
  const check = (ok, where, msg) => ok || problems.push(`${where}: ${msg}`)

  for (const mod of modules) check(sectionOrder.has(mod.section), mod.id, `unknown section "${mod.section}"`)

  const termOwners = {}
  for (const mod of modules) {
    for (const [id, entry] of Object.entries(mod.terms ?? {})) {
      check(!termOwners[id], `${mod.id} › term ${id}`, `already defined in ${termOwners[id]}`)
      check(entry.term && entry.definition, `${mod.id} › term ${id}`, 'needs term and definition')
      termOwners[id] = mod.id
    }
  }
  const introduced = new Set()

  const FORMATS = new Set(['concept', 'document', 'story', 'spot', 'sort', 'call'])
  const DOC_KINDS = new Set(['paystub', 'bill', 'receipt', 'statement'])

  for (const lesson of lessons) {
    check(!seen.has(lesson.id), lesson.id, 'duplicate lesson id')
    seen.add(lesson.id)
    check(Array.isArray(lesson.steps), lesson.id, 'missing steps array')
    check(FORMATS.has(lesson.format), lesson.id, `unknown format "${lesson.format}"`)
    if (lesson.format === 'story') check(lesson.story?.title && lesson.story?.body, lesson.id, 'story lessons need a story')
    if (lesson.story) {
      for (const id of termsIn(lesson.story.body)) {
        check(glossary[id], lesson.id, `unknown term [[${id}]] in story`)
        introduced.add(id)
      }
    }

    for (const step of lesson.steps ?? []) {
      const where = `${lesson.id} › ${step.id ?? '(no id)'}`
      check(step.id && !seen.has(step.id), where, 'missing or duplicate step id')
      seen.add(step.id)
      for (const id of allText(step).flatMap(termsIn)) check(glossary[id], where, `unknown term [[${id}]]`)
      for (const id of stepTerms(step)) introduced.add(id)
      for (const id of [...termsIn(step.explain), ...[...(step.choices ?? []), ...(step.items ?? [])].flatMap(termsIn)]) {
        check(introduced.has(id), where, `term "${id}" is used before any step teaches it`)
      }
      for (const doc of stepDocs(step)) {
        check(DOC_KINDS.has(doc.kind), where, `unknown document kind "${doc.kind}"`)
        check(doc.title && doc.lines?.length, where, 'document needs a title and lines')
        check(new Set(doc.lines?.map((l) => l.id)).size === doc.lines?.length, where, 'document line ids must be unique')
        check(doc.lines?.every((l) => l.id && Number.isFinite(l.amount)), where, 'every document line needs an id and an amount')
      }
      if (step.why) check(step.why.length === step.choices?.length, where, 'why[] needs one entry per choice')
      switch (step.type) {
        case 'info':
          check(step.title && step.body, where, 'info needs title and body')
          break
        case 'multiple_choice':
        case 'fill_blank':
          check(step.choices?.length >= 2, where, 'needs 2+ choices')
          check(Number.isInteger(step.answer) && step.choices?.[step.answer] !== undefined, where, 'answer must index into choices')
          if (step.type === 'fill_blank') check(step.prompt?.split('___').length === 2, where, 'prompt needs exactly one ___')
          break
        case 'true_false':
          check(typeof step.answer === 'boolean', where, 'answer must be true or false')
          break
        case 'number':
          check(Number.isFinite(step.answer), where, 'answer must be a number')
          break
        case 'order':
          check(step.items?.length >= 3, where, 'needs 3+ items')
          check(new Set(step.items).size === step.items?.length, where, 'items must be unique')
          break
        case 'match':
          check(step.pairs?.length >= 3, where, 'needs 3+ pairs')
          check(new Set(step.pairs?.map((p) => p[1])).size === step.pairs?.length, where, 'right-hand sides must be unique')
          break
        case 'spot':
          check(step.doc, where, 'spot needs a doc')
          check(step.doc?.lines?.some((l) => l.id === step.answer), where, 'spot answer must be a line id on the doc')
          break
        case 'sort':
          check(step.buckets?.length >= 2, where, 'needs 2+ buckets')
          check(step.items?.length >= 3, where, 'needs 3+ items')
          check(step.items?.every(([, b]) => Number.isInteger(b) && step.buckets?.[b] !== undefined), where, 'every item needs a valid bucket index')
          break
        case 'allocate': {
          const cats = step.categories ?? []
          check(Number.isFinite(step.total) && step.step > 0 && cats.length >= 2, where, 'needs total, step and 2+ categories')
          const low = cats.reduce((sum, c) => sum + (c.fixed ?? c.min ?? 0), 0)
          const high = cats.reduce((sum, c) => sum + (c.fixed ?? c.max ?? Infinity), 0)
          check(low <= step.total && step.total <= high, where, 'no amounts satisfy every rule')
          const flexible = step.total - cats.reduce((sum, c) => sum + (c.fixed ?? 0), 0)
          check(flexible % step.step === 0 && cats.every((c) => (c.min ?? 0) % step.step === 0), where, 'amounts must be reachable in steps')
          break
        }
        default:
          problems.push(`${where}: unknown step type "${step.type}"`)
      }
    }
  }
  for (const id of Object.keys(glossary)) check(introduced.has(id), `term ${id}`, 'defined but never taught')
  return problems
}

if (import.meta.env.DEV && typeof window !== 'undefined') {
  const problems = validateContent()
  if (problems.length) console.warn(`[content] ${problems.length} problem(s):\n${problems.join('\n')}`)
}
