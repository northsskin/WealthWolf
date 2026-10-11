import { useEffect, useReducer, useRef } from 'react'
import { Calculator as CalcIcon, X } from 'lucide-react'
import { CALC_KEYS, calcDisplay, calcReducer, calcValue, formatTape, initialCalc, toAnswer } from '../../lib/calc.js'
import { formatMoney } from '../../lib/session.js'
import './Calculator.css'

// Keyboard → key. Anything typed inside the panel stays inside the panel, so
// the lesson's own shortcuts (1–9 to pick, Enter to check) don't fire.
const KEYMAP = { '-': '−', '*': '×', x: '×', X: '×', '/': '÷', Enter: '=', '=': '=', Backspace: '⌫', Delete: 'C', c: 'C', C: 'C', ',': null }
const OPS = new Set(['+', '−', '×', '÷'])

// The tab on the lesson's right edge, like an index tab on a ledger.
export function CalculatorTab({ onOpen }) {
  return (
    <button className="calc-tab" onClick={onOpen} aria-label="Open the calculator" aria-controls="calculator">
      <CalcIcon />
      <span>Calculator</span>
    </button>
  )
}

export default function Calculator({ open, onClose, canUse, onUse }) {
  const [state, press] = useReducer(calcReducer, initialCalc)
  const panel = useRef(null)
  const tape = useRef(null)
  const value = calcValue(state)

  useEffect(() => {
    if (open) panel.current?.focus()
  }, [open])

  useEffect(() => {
    tape.current?.scrollTo({ top: tape.current.scrollHeight })
  }, [state.tape.length])

  function onKeyDown(event) {
    if (event.key === 'Tab' || event.metaKey || event.ctrlKey) return
    event.stopPropagation()
    if (event.key === 'Escape') return onClose()
    const key = event.key in KEYMAP ? KEYMAP[event.key] : event.key
    if (key && CALC_KEYS.includes(key)) {
      event.preventDefault()
      press(key)
    }
  }

  return (
    <aside
      id="calculator"
      ref={panel}
      className={open ? 'calc is-open' : 'calc'}
      aria-label="Calculator"
      tabIndex={-1}
      inert={!open}
      onKeyDown={onKeyDown}
    >
      <header className="calc__head">
        <p className="display calc__title">Calculator</p>
        <button className="calc__close" onClick={onClose} aria-label="Close the calculator">
          <X />
        </button>
      </header>

      <ol className="calc__tape" ref={tape} aria-label="Tape" aria-live="polite">
        {state.tape.length === 0 && (
          <li className="calc__hint">Your working prints here, like an adding-machine tape. Tap the keys or just type.</li>
        )}
        {state.tape.map((line, i) =>
          line.total !== undefined ? (
            <li key={i} className="calc__line calc__line--total">
              <span>=</span>
              <span className="figure">{formatTape(line.total)}</span>
            </li>
          ) : (
            <li key={i} className="calc__line">
              <span>{line.sign}</span>
              <span className="figure">{formatTape(line.value)}</span>
            </li>
          ),
        )}
      </ol>

      <p className={state.error ? 'calc__display is-error' : 'calc__display'} aria-label="Display">
        <span className="calc__pending">{state.op && !state.done ? state.op : ''}</span>
        <span className="figure">{calcDisplay(state)}</span>
      </p>

      {canUse && (
        <button className="btn btn--block calc__use" onClick={() => onUse(toAnswer(value))} disabled={value === null}>
          Use {value === null ? 'this' : formatMoney(Math.round(value * 100) / 100)} as my answer
        </button>
      )}

      <div className="calc__keys">
        {CALC_KEYS.map((key) => (
          <button
            key={key}
            type="button"
            className={`calc__key${OPS.has(key) ? ' is-op' : ''}${key === '=' ? ' is-equals' : ''}${key === 'C' || key === '⌫' ? ' is-edit' : ''}`}
            onClick={() => press(key)}
            aria-label={{ '⌫': 'Delete last digit', '±': 'Make negative or positive', C: 'Clear' }[key]}
          >
            {key}
          </button>
        ))}
      </div>
    </aside>
  )
}
