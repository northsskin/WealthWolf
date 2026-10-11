import { useEffect, useRef } from 'react'

// Number keys 1–9 pick the matching option, Duolingo-style.
export function useDigitKeys(count, onPick, enabled) {
  const pick = useRef(onPick)
  pick.current = onPick

  useEffect(() => {
    if (!enabled) return
    function onKey(event) {
      if (event.metaKey || event.ctrlKey || event.altKey) return
      if (event.target instanceof HTMLInputElement || event.target instanceof HTMLTextAreaElement) return
      const n = Number(event.key)
      if (Number.isInteger(n) && n >= 1 && n <= count) {
        event.preventDefault()
        pick.current(n - 1)
      }
    }
    window.addEventListener('keydown', onKey)
    return () => window.removeEventListener('keydown', onKey)
  }, [count, enabled])
}

// Visual state of one option once the answer has (or hasn't) been checked.
export function optionState({ value, picked, answer, revealed }) {
  if (revealed) {
    if (value === answer) return 'is-correct'
    if (value === picked) return 'is-wrong'
    return 'is-dim'
  }
  return value === picked ? 'is-selected' : ''
}
