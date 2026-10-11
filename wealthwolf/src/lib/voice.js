import manifest from './voice-manifest.json'
import { getState } from '../store/store.js'
import { modules } from './content.js'
import { barkLines, voiceLinesFor } from './voiceLines.js'

// The Wolf's voice: pre-rendered clips in public/voice/, listed in the manifest.
// One clip plays at a time; a missing clip is simply silent.
let current = null
let pending = null

export function hasVoice(key) {
  return Boolean(manifest.clips[key])
}

export function stopVoice() {
  clearTimeout(pending)
  pending = null
  if (current) {
    current.pause()
    current = null
  }
}

export function playVoice(key, { delay = 0 } = {}) {
  stopVoice()
  const clip = manifest.clips[key]
  if (!clip || !getState().settings.sound) return
  const start = () => {
    const audio = new Audio(`${import.meta.env.BASE_URL}voice/${clip.file}`)
    current = audio
    audio.play().catch(() => {}) // autoplay can be refused before any tap; stay quiet
  }
  if (delay) pending = setTimeout(start, delay)
  else start()
}

// Dev check: once a module has any clips, every line in it should have a fresh one.
if (import.meta.env.DEV) {
  const voiced = modules.filter((m) => voiceLinesFor([m]).some((l) => manifest.clips[l.key]))
  const lines = [...voiceLinesFor(voiced), ...(voiced.length ? barkLines() : [])]
  const missing = lines.filter((l) => !manifest.clips[l.key]).map((l) => l.key)
  const stale = lines.filter((l) => manifest.clips[l.key] && manifest.clips[l.key].hash !== l.hash).map((l) => l.key)
  if (missing.length || stale.length) {
    console.warn(`[voice] ${missing.length} missing, ${stale.length} stale (text changed since recording). Run node scripts/voice-lines.mjs.\n${[...missing, ...stale].join('\n')}`)
  }
}
