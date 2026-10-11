// Lists the lines the Wolf should speak and groups them into ElevenLabs takes.
//   node scripts/voice-lines.mjs [moduleId ...]      (default: money-fundamentals)
// Writes scripts/voice/batches.json and prints each take's prompt, lines
// separated by [long pause] so scripts/split-voice.mjs can cut them apart.
import { readFileSync, readdirSync, writeFileSync, mkdirSync } from 'node:fs'
import { barkLines, voiceLinesFor } from '../src/lib/voiceLines.js'

// Units live one folder per section: src/data/<section>/<unit>.json.
const dataDir = new URL('../src/data/', import.meta.url)
const modules = readdirSync(dataDir, { withFileTypes: true })
  .filter((entry) => entry.isDirectory())
  .flatMap((dir) =>
    readdirSync(new URL(`${dir.name}/`, dataDir))
      .filter((f) => f.endsWith('.json'))
      .map((f) => JSON.parse(readFileSync(new URL(`${dir.name}/${f}`, dataDir), 'utf8'))),
  )
const wanted = process.argv.slice(2)
const chosen = modules.filter((m) => (wanted.length ? wanted : ['money-fundamentals']).includes(m.id))

const manifest = JSON.parse(readFileSync(new URL('../src/lib/voice-manifest.json', import.meta.url), 'utf8'))
const fresh = (line) => manifest.clips[line.key]?.hash === line.hash

const lines = voiceLinesFor(chosen).filter((l) => !fresh(l))
const barks = barkLines().filter((l) => !fresh(l))
const stories = lines.filter((l) => l.key.endsWith('-story'))
const spoken = lines.filter((l) => !l.key.endsWith('-story'))

// Stories are read as one take each: their paragraph pauses would confuse the splitter.
const batches = []
const MAX = 16
for (let i = 0; i < spoken.length; i += MAX) batches.push({ name: `lines-${batches.length + 1}`, lines: spoken.slice(i, i + MAX) })
if (barks.length) batches.push({ name: 'barks', lines: barks })
for (const story of stories) batches.push({ name: story.key, lines: [story] })

for (const batch of batches) batch.prompt = batch.lines.map((l) => l.text).join(' [long pause] ')

mkdirSync(new URL('./voice/', import.meta.url), { recursive: true })
writeFileSync(new URL('./voice/batches.json', import.meta.url), JSON.stringify(batches, null, 2))
let chars = 0
for (const batch of batches) {
  chars += batch.prompt.length
  console.log(`\n== ${batch.name}: ${batch.lines.length} line(s), ${batch.prompt.length} chars\n${batch.prompt}`)
}
console.log(`\n${batches.length} take(s), ${chars} characters in total.`)
