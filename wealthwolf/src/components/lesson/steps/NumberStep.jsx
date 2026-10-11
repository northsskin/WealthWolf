import { useEffect, useRef } from 'react'
import { Rich } from '../../Rich.jsx'

// Keep what the player types tidy: one leading minus, digits, one decimal
// point, and thousands separators added as they go.
function tidy(raw) {
  const negative = /^\s*[-−–]/.test(raw)
  const [whole = '', ...rest] = raw.replace(/[^\d.]/g, '').split('.')
  const grouped = whole.replace(/^0+(?=\d)/, '').replace(/\B(?=(\d{3})+(?!\d))/g, ',')
  const decimals = rest.length ? `.${rest.join('').slice(0, 2)}` : ''
  return (negative ? '-' : '') + grouped + decimals
}

export default function NumberStep({ card, answer, setAnswer, revealed, correct }) {
  const { step } = card
  const input = useRef(null)
  const value = answer ?? ''

  useEffect(() => {
    input.current?.focus()
  }, [card.key])

  function toggleSign() {
    setAnswer(value.startsWith('-') ? value.slice(1) : `-${value}`)
    input.current?.focus()
  }

  let state = ''
  if (revealed) state = correct ? 'is-correct' : 'is-wrong'

  return (
    <>
      <h2 className="step__prompt">
        <Rich text={step.prompt} />
      </h2>
      <div className={`numfield ${state}`}>
        <button
          type="button"
          className="numfield__sign"
          onClick={toggleSign}
          disabled={revealed}
          aria-label="Make negative or positive"
        >
          +/−
        </button>
        {step.unit === '$' && <span className="numfield__prefix">$</span>}
        <input
          ref={input}
          className="numfield__input tabular"
          inputMode="decimal"
          autoComplete="off"
          placeholder="0"
          value={value}
          onChange={(e) => setAnswer(tidy(e.target.value))}
          disabled={revealed}
          aria-label="Your answer"
        />
        {step.unit && step.unit !== '$' && <span className="numfield__unit">{step.unit}</span>}
      </div>
      <p className="numfield__hint">Just the number. Press Enter to check.</p>
    </>
  )
}
