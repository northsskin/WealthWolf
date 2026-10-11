// An adding-machine calculator: immediate execution (3,200 − 2,900 = 300),
// with every number printed to a tape alongside the operation applied to it.

export const CALC_KEYS = ['C', '⌫', '÷', '×', '7', '8', '9', '−', '4', '5', '6', '+', '1', '2', '3', '=', '±', '0', '.']

export const initialCalc = { entry: '', acc: null, op: null, tape: [], done: false, error: null }

const MAX_DIGITS = 12
const MAX_TAPE = 40

// Floating-point noise off (0.1 + 0.2), but no rounding a person would notice.
const clean = (n) => Math.round(n * 1e9) / 1e9

function apply(acc, op, value) {
  switch (op) {
    case '+':
      return clean(acc + value)
    case '−':
      return clean(acc - value)
    case '×':
      return clean(acc * value)
    case '÷':
      return value === 0 ? null : clean(acc / value)
    default:
      return value
  }
}

const print = (tape, ...lines) => [...tape, ...lines].slice(-MAX_TAPE)

// After "=", typing a digit starts a fresh sum (the tape stays).
const fresh = (s) => (s.done ? { ...s, acc: null, op: null, done: false, entry: '' } : s)

export function calcReducer(state, key) {
  const s = state.error ? { ...initialCalc, tape: state.tape } : state

  if (/^\d$/.test(key)) {
    const t = fresh(s)
    if (t.entry.replace(/[-.]/g, '').length >= MAX_DIGITS) return t
    const entry = t.entry === '0' ? key : t.entry === '-0' ? `-${key}` : t.entry + key
    return { ...t, entry }
  }

  switch (key) {
    case '.': {
      const t = fresh(s)
      if (t.entry.includes('.')) return t
      return { ...t, entry: `${t.entry === '' || t.entry === '-' ? `${t.entry}0` : t.entry}.` }
    }
    case '+':
    case '−':
    case '×':
    case '÷': {
      if (s.done) return { ...s, op: key, done: false }
      if (s.entry === '' || s.entry === '-') return s.acc === null ? s : { ...s, op: key }
      const value = Number(s.entry)
      if (s.acc === null) return { ...s, acc: value, op: key, entry: '', tape: print(s.tape, { sign: '', value }) }
      const acc = apply(s.acc, s.op, value)
      if (acc === null) return { ...initialCalc, tape: s.tape, error: 'Can’t divide by zero' }
      return { ...s, acc, op: key, entry: '', tape: print(s.tape, { sign: s.op, value }) }
    }
    case '=': {
      if (s.entry === '' || s.entry === '-') return s
      const value = Number(s.entry)
      if (s.acc === null || s.op === null) {
        return { ...s, acc: value, op: null, entry: '', done: true, tape: print(s.tape, { sign: '', value }, { total: value }) }
      }
      const acc = apply(s.acc, s.op, value)
      if (acc === null) return { ...initialCalc, tape: s.tape, error: 'Can’t divide by zero' }
      return { ...s, acc, op: null, entry: '', done: true, tape: print(s.tape, { sign: s.op, value }, { total: acc }) }
    }
    case 'C':
      return initialCalc
    case '⌫':
      return s.done ? s : { ...s, entry: s.entry.slice(0, -1) }
    case '±': {
      if (s.done) return { ...s, acc: null, op: null, done: false, entry: String(-s.acc) }
      if (s.entry === '') return { ...s, entry: '-' }
      return { ...s, entry: s.entry.startsWith('-') ? s.entry.slice(1) : `-${s.entry}` }
    }
    default:
      return s
  }
}

// The number the calculator is showing, as a number (null when there's nothing).
export function calcValue(s) {
  if (s.error) return null
  if (s.entry !== '' && s.entry !== '-') return Number(s.entry)
  return s.acc
}

// What the display shows: the entry as typed (with thousands separators), or the result.
export function calcDisplay(s) {
  if (s.error) return s.error
  if (s.entry !== '') {
    const [whole, dec] = s.entry.replace('-', '').split('.')
    const grouped = (whole || '0').replace(/\B(?=(\d{3})+(?!\d))/g, ',')
    return `${s.entry.startsWith('-') ? '−' : ''}${grouped}${dec !== undefined ? `.${dec}` : ''}`
  }
  return formatTape(s.acc ?? 0)
}

export function formatTape(n) {
  return `${n < 0 ? '−' : ''}${Math.abs(n).toLocaleString('en-US', { maximumFractionDigits: 6 })}`
}

// A value written the way the number-answer field expects it ("2,158.8", "-3,000").
export function toAnswer(n) {
  const rounded = Math.round(n * 100) / 100
  return `${rounded < 0 ? '-' : ''}${Math.abs(rounded).toLocaleString('en-US', { maximumFractionDigits: 2 })}`
}
