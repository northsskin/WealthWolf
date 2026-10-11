import { useEffect, useRef, useState } from 'react'
import { Rich } from '../../Rich.jsx'
import { plain } from '../../../lib/content.js'

// Tap a term, then its partner. Wrong pairs flash red and reset; they don't
// cost hearts, but they do count against the question's spaced-repetition box.
export default function MatchStep({ card, onPair, onSolved, revealed }) {
  const { step, left, right } = card
  const [selected, setSelected] = useState(null) // { side: 'L' | 'R', pair }
  const [matched, setMatched] = useState([])
  const [miss, setMiss] = useState(null) // { l, r }
  const misses = useRef(0)
  const timer = useRef(null)

  useEffect(() => () => clearTimeout(timer.current), [])

  function pick(side, pair) {
    if (revealed || miss || matched.includes(pair)) return
    if (!selected || selected.side === side) {
      setSelected(selected?.side === side && selected.pair === pair ? null : { side, pair })
      return
    }
    const l = side === 'L' ? pair : selected.pair
    const r = side === 'R' ? pair : selected.pair
    setSelected(null)
    if (l === r) {
      const next = [...matched, l]
      setMatched(next)
      onPair(true, next.length)
      if (next.length === step.pairs.length) timer.current = setTimeout(() => onSolved(misses.current), 350)
    } else {
      misses.current += 1
      setMiss({ l, r })
      onPair(false)
      timer.current = setTimeout(() => setMiss(null), 550)
    }
  }

  function stateFor(side, pair) {
    if (matched.includes(pair)) return 'is-matched'
    if (miss && (side === 'L' ? miss.l : miss.r) === pair) return 'is-wrong'
    if (selected?.side === side && selected.pair === pair) return 'is-selected'
    return ''
  }

  const column = (side, indices, textIndex) => (
    <div className="match__col">
      {indices.map((pair) => (
        <button
          key={pair}
          className={`option match__item ${stateFor(side, pair)}`}
          onClick={() => pick(side, pair)}
          disabled={revealed || matched.includes(pair)}
        >
          {plain(step.pairs[pair][textIndex])}
        </button>
      ))}
    </div>
  )

  return (
    <>
      <h2 className="step__prompt">
        <Rich text={step.prompt} />
      </h2>
      <div className="match">
        {column('L', left, 0)}
        {column('R', right, 1)}
      </div>
    </>
  )
}
