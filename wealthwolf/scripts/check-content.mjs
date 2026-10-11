// Checks every unit in src/data without opening a browser: the same rules the
// app warns about in the console, plus a few extra authoring checks.
//   npm run check
import { createServer } from 'vite'

const server = await createServer({ server: { middlewareMode: true }, appType: 'custom', logLevel: 'error' })
const plain = (text) => text.replace(/\[\[([^\]|]+)(?:\|[^\]]+)?\]\]/g, '$1').replace(/\*\*(.+?)\*\*/g, '$1').trim()

try {
  const { validateContent, sections, lessons, glossary } = await server.ssrLoadModule('/src/lib/content.js')
  const problems = validateContent()

  // A trial's own question must not repeat a lesson question word for word:
  // the trial also draws lesson questions, and the player would see both.
  for (const trial of lessons.filter((l) => l.type === 'boss')) {
    const scope = lessons.filter((l) => l.type === 'lesson' && (trial.scope === 'section' ? l.sectionId === trial.sectionId : l.moduleId === trial.moduleId))
    const prompts = new Set(scope.flatMap((l) => l.steps).filter((s) => s.prompt).map((s) => plain(s.prompt)))
    for (const step of trial.steps) if (step.prompt && prompts.has(plain(step.prompt))) problems.push(`${step.id}: same prompt as a lesson question`)
  }

  for (const section of sections) {
    const own = lessons.filter((l) => l.sectionId === section.id && l.type === 'lesson')
    const thin = section.units.filter((u) => u.lessons.filter((l) => l.type === 'lesson').length < 8).map((u) => u.id)
    console.log(`Section ${section.number} ${section.title}: ${section.units.length} units, ${own.length} lessons${section.trial ? ', section trial' : ''}${thin.length ? `  (under 8 lessons: ${thin.join(', ')})` : ''}`)
  }
  console.log(`${lessons.filter((l) => l.type === 'lesson').length} lessons, ${Object.keys(glossary).length} glossary words`)

  if (problems.length) {
    console.error(`\n${problems.length} problem(s):\n${problems.map((p) => `  ${p}`).join('\n')}`)
    process.exitCode = 1
  } else {
    console.log('\nNo problems found.')
  }
} finally {
  await server.close()
}
