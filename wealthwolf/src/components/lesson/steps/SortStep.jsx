import { useEffect, useRef, useState } from 'react'
import { Rich } from '../../Rich.jsx'
import { plain } from '../../../lib/content.js'
import { useDigitKeys } from './useDigitKeys.js'

// One card at a time: tap the bucket it belongs in. A wrong bucket shakes and
// the card stays put; like matching, misses cost no hearts but do count
// against the question in spaced repetition.
export default function SortStep({ card, onPair, onSolved, revealed }) {
  const { step, order } = card
  const [placed, setPlaced] = useState([]) // item indexes, in the order sorted
  const [miss, setMiss] = useState(null) // bucket index that was just wrong
  const misses = useRef(0)
  const timer = useRef(null)
  useEffect(() => () => clearTimeout(timer.current), [])

  const current = order[placed.length]
  const done = current === undefined

  function place(bucket) {
    if (done || revealed || miss !== null) return
    const [, right] = step.items[current]
    if (bucket === right) {
      const next = [...placed, current]
      setPlaced(next)
      onPair(true, next.length)
      if (next.length === step.items.length) timer.current = setTimeout(() => onSolved(misses.current), 350)
    } else {
      misses.current += 1
      setMiss(bucket)
      onPair(false)
      timer.current = setTimeout(() => setMiss(null), 500)
    }
  }
  useDigitKeys(step.buckets.length, place, !done && !revealed)

  return (
    <>
      <h2 className="step__prompt">
        <Rich text={step.prompt} />
      </h2>
      <div className="sort">
        <div className="sort__deck" aria-live="polite">
          {done ? (
            <p className="sort__done">All sorted.</p>
          ) : (
            <p key={current} className={miss !== null ? 'sort__card is-wrong' : 'sort__card'}>
              {plain(step.items[current][0])}
            </p>
          )}
          <p className="figure sort__count">
            {Math.min(placed.length + 1, step.items.length)} / {step.items.length}
          </p>
        </div>
        <div className="sort__buckets" style={{ '--buckets': step.buckets.length }}>
          {step.buckets.map((bucket, b) => (
            <button
              key={bucket}
              className={`sort__bucket${miss === b ? ' is-wrong' : ''}`}
              onClick={() => place(b)}
              disabled={done || revealed}
            >
              <span className="sort__bucket-head">
                <kbd className="option__key">{b + 1}</kbd>
                <span className="display sort__bucket-name">{bucket}</span>
              </span>
              <span className="sort__chips">
                {placed
                  .filter((i) => step.items[i][1] === b)
                  .map((i) => (
                    <span key={i} className="sort__chip">
                      {plain(step.items[i][0])}
                    </span>
                  ))}
              </span>
            </button>
          ))}
        </div>
      </div>
    </>
  )
}
