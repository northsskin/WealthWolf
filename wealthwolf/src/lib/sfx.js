import { getState } from '../store/store.js'

// Tiny synthesized sound effects: no audio files, nothing to download.
let ctx = null

function audio() {
  if (!getState().settings.sound) return null
  if (!ctx) {
    const AudioCtx = window.AudioContext || window.webkitAudioContext
    if (!AudioCtx) return null
    ctx = new AudioCtx()
  }
  if (ctx.state === 'suspended') ctx.resume()
  return ctx
}

function tone(ac, freq, at, duration, { type = 'triangle', gain = 0.12, slideTo } = {}) {
  const start = ac.currentTime + at
  const osc = ac.createOscillator()
  const env = ac.createGain()
  osc.type = type
  osc.frequency.setValueAtTime(freq, start)
  if (slideTo) osc.frequency.exponentialRampToValueAtTime(slideTo, start + duration)
  env.gain.setValueAtTime(0.0001, start)
  env.gain.exponentialRampToValueAtTime(gain, start + 0.012)
  env.gain.exponentialRampToValueAtTime(0.0001, start + duration)
  osc.connect(env).connect(ac.destination)
  osc.start(start)
  osc.stop(start + duration + 0.05)
}

const semitone = (base, steps) => base * 2 ** (steps / 12)

export const sfx = {
  correct() {
    const ac = audio()
    if (!ac) return
    tone(ac, 880, 0, 0.12)
    tone(ac, 1318.5, 0.08, 0.26)
  },
  wrong() {
    const ac = audio()
    if (!ac) return
    tone(ac, 220, 0, 0.3, { type: 'sawtooth', gain: 0.045, slideTo: 140 })
  },
  pair(n) {
    const ac = audio()
    if (!ac) return
    tone(ac, semitone(659.25, n * 2), 0, 0.16, { gain: 0.1 })
  },
  complete() {
    const ac = audio()
    if (!ac) return
    ;[523.25, 659.25, 783.99, 1046.5, 1318.5].forEach((f, i) => tone(ac, f, i * 0.08, 0.4, { gain: 0.1 }))
  },
  fail() {
    const ac = audio()
    if (!ac) return
    ;[392, 329.63, 261.63].forEach((f, i) => tone(ac, f, i * 0.16, 0.35, { type: 'sawtooth', gain: 0.04 }))
  },
}
