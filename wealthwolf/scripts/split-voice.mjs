// Cuts one ElevenLabs take into a clip per line and records them in the manifest.
//   node scripts/split-voice.mjs <batch-name> <take.mp3> [--voice <voice name>]
// The take must read the batch's lines in order with [long pause] between them.
// Exits without writing anything if the number of segments doesn't match.
import { execFileSync } from 'node:child_process'
import { readFileSync, writeFileSync, mkdirSync } from 'node:fs'
import ffmpeg from 'ffmpeg-static'

const [name, take, ...rest] = process.argv.slice(2)
const voiceName = rest[rest.indexOf('--voice') + 1]
const batches = JSON.parse(readFileSync(new URL('./voice/batches.json', import.meta.url), 'utf8'))
const batch = batches.find((b) => b.name === name)
if (!batch || !take) {
  console.error('usage: node scripts/split-voice.mjs <batch-name> <take.mp3> [--voice name]')
  process.exit(1)
}

const MIN_GAP = 0.8 // seconds of silence that separate two lines
const PAD = 0.12 // keep a breath either side of each clip

// Find the silences, then take the stretches of speech between them.
const log = execFileSync(ffmpeg, ['-hide_banner', '-i', take, '-af', `silencedetect=noise=-38dB:d=${MIN_GAP}`, '-f', 'null', '-'], {
  encoding: 'utf8',
  stdio: ['ignore', 'pipe', 'pipe'],
}).toString()
const probe = execFileSync(ffmpeg, ['-hide_banner', '-i', take], { encoding: 'utf8', stdio: ['ignore', 'pipe', 'pipe'] }).toString()
const stderr = (cmd) => {
  try {
    execFileSync(ffmpeg, cmd, { stdio: ['ignore', 'pipe', 'pipe'] })
    return ''
  } catch (e) {
    return e.stderr.toString()
  }
}
const details = stderr(['-hide_banner', '-i', take, '-af', `silencedetect=noise=-38dB:d=${MIN_GAP}`, '-f', 'null', '-']) || log || probe
const durationMatch = stderr(['-hide_banner', '-i', take]).match(/Duration: (\d+):(\d+):([\d.]+)/)
const duration = durationMatch ? +durationMatch[1] * 3600 + +durationMatch[2] * 60 + +durationMatch[3] : 0

const starts = [...details.matchAll(/silence_start: ([\d.]+)/g)].map((m) => +m[1])
const ends = [...details.matchAll(/silence_end: ([\d.]+)/g)].map((m) => +m[1])
const segments = []
let cursor = 0
for (let i = 0; i < starts.length; i++) {
  if (starts[i] - cursor > 0.2) segments.push([cursor, starts[i]])
  cursor = ends[i] ?? duration
}
if (duration - cursor > 0.2) segments.push([cursor, duration])

if (segments.length !== batch.lines.length) {
  console.error(`✗ ${name}: found ${segments.length} segments for ${batch.lines.length} lines. Nothing written.`)
  console.error(segments.map(([a, b]) => `${a.toFixed(2)}–${b.toFixed(2)}`).join('  '))
  process.exit(2)
}

const outDir = new URL('../public/voice/', import.meta.url)
mkdirSync(outDir, { recursive: true })
const manifestUrl = new URL('../src/lib/voice-manifest.json', import.meta.url)
const manifest = JSON.parse(readFileSync(manifestUrl, 'utf8'))
if (voiceName) manifest.voice = voiceName

batch.lines.forEach((line, i) => {
  const [a, b] = segments[i]
  const from = Math.max(0, a - PAD)
  const to = Math.min(duration, b + PAD)
  const file = `${line.key}.mp3`
  execFileSync(ffmpeg, ['-y', '-hide_banner', '-loglevel', 'error', '-ss', from.toFixed(3), '-to', to.toFixed(3), '-i', take, '-ac', '1', '-ar', '44100', '-b:a', '64k', new URL(file, outDir).pathname])
  manifest.clips[line.key] = { file, hash: line.hash, seconds: +(to - from).toFixed(2) }
  console.log(`✓ ${line.key}  ${(to - from).toFixed(2)}s  “${line.text.slice(0, 60)}${line.text.length > 60 ? '…' : ''}”`)
})
writeFileSync(manifestUrl, JSON.stringify(manifest, null, 2) + '\n')
console.log(`\n${batch.lines.length} clips written to public/voice/, manifest updated.`)
