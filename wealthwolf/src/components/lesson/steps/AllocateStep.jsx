import { Minus, Plus } from 'lucide-react'
import { Rich } from '../../Rich.jsx'
import { allocated, categoryOk, formatMoney, parseNumber } from '../../../lib/session.js'

function ruleText(c) {
  if (c.fixed !== undefined) return 'Fixed'
  if (c.min !== undefined && c.max !== undefined) return `${formatMoney(c.min)} to ${formatMoney(c.max)}`
  if (c.min !== undefined) return `At least ${formatMoney(c.min)}`
  if (c.max !== undefined) return `At most ${formatMoney(c.max)}`
  return 'Your call'
}

// The budget builder: give every dollar a job. Steppers move money in the
// lesson's step size, the amount can be typed directly, and "rest" drops
// whatever's unassigned into that row.
export default function AllocateStep({ card, answer, setAnswer, revealed }) {
  const { step } = card
  const amounts = answer ?? step.categories.map((c) => c.fixed ?? 0)
  const left = step.total - allocated(amounts)

  // Updaters work from the latest amounts, so fast taps never drop a step.
  function update(i, change) {
    setAnswer((current) => {
      const next = [...(current ?? amounts)]
      const left = step.total - allocated(next)
      next[i] = Math.max(0, change(next[i], left))
      return next
    })
  }

  return (
    <>
      <h2 className="step__prompt">
        <Rich text={step.prompt} />
      </h2>
      <div className="alloc">
        <p className="alloc__total">
          <span>To split</span>
          <span className="figure">{formatMoney(step.total)}</span>
        </p>
        {step.categories.map((c, i) => {
          let state = ''
          if (revealed) state = categoryOk(c, amounts[i]) ? 'is-correct' : 'is-wrong'
          return (
            <div key={c.label} className={`alloc__row ${state}`}>
              <p className="alloc__label">
                {c.label}
                <span className="alloc__rule">{ruleText(c)}</span>
              </p>
              {c.fixed !== undefined ? (
                <span className="figure alloc__fixed">{formatMoney(c.fixed)}</span>
              ) : (
                <div className="alloc__controls">
                  {left > 0 && !revealed && (
                    <button className="alloc__rest" onClick={() => update(i, (amount, rest) => amount + Math.max(rest, 0))}>
                      + rest
                    </button>
                  )}
                  <div className="alloc__stepper">
                    <button
                      aria-label={`${formatMoney(step.step)} less for ${c.label}`}
                      onClick={() => update(i, (amount) => amount - step.step)}
                      disabled={revealed || amounts[i] <= 0}
                    >
                      <Minus />
                    </button>
                    <input
                      className="figure"
                      inputMode="numeric"
                      aria-label={`${c.label} amount`}
                      value={amounts[i].toLocaleString('en-US')}
                      onChange={(e) => {
                        const typed = parseNumber(e.target.value.replace(/[^\d]/g, '') || '0') ?? 0
                        update(i, () => typed)
                      }}
                      disabled={revealed}
                    />
                    <button
                      aria-label={`${formatMoney(step.step)} more for ${c.label}`}
                      onClick={() => update(i, (amount, rest) => amount + Math.min(step.step, rest))}
                      disabled={revealed || left <= 0}
                    >
                      <Plus />
                    </button>
                  </div>
                </div>
              )}
            </div>
          )
        })}
        <p className={left === 0 ? 'alloc__left is-zero' : left < 0 ? 'alloc__left is-over' : 'alloc__left'}>
          <span>{left < 0 ? 'Over by' : 'Left to assign'}</span>
          <span className="figure">{formatMoney(Math.abs(left))}</span>
        </p>
      </div>
    </>
  )
}
