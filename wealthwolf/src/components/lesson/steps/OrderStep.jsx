import { Rich } from '../../Rich.jsx'
import { plain } from '../../../lib/content.js'
import { useDigitKeys } from './useDigitKeys.js'

export default function OrderStep({ card, answer, setAnswer, revealed }) {
  const { step, order } = card
  const placed = answer ?? []
  const bank = order.filter((itemIndex) => !placed.includes(itemIndex))

  const add = (itemIndex) => setAnswer([...placed, itemIndex])
  const remove = (position) => setAnswer(placed.filter((_, i) => i !== position))
  useDigitKeys(bank.length, (k) => add(bank[k]), !revealed)

  return (
    <>
      <h2 className="step__prompt">
        <Rich text={step.prompt} />
      </h2>
      <ol className="order__slots" aria-label="Your order">
        {step.items.map((_, position) => {
          const itemIndex = placed[position]
          let state = ''
          if (revealed && itemIndex !== undefined) state = itemIndex === position ? 'is-correct' : 'is-wrong'
          return (
            <li key={position} className="order__slot">
              <span className="order__num tabular">{position + 1}</span>
              {itemIndex === undefined ? (
                <span className="order__empty" />
              ) : (
                <button
                  className={`ordtile ${state}`}
                  onClick={() => remove(position)}
                  disabled={revealed}
                  aria-label={`${plain(step.items[itemIndex])}. Tap to remove.`}
                >
                  {plain(step.items[itemIndex])}
                </button>
              )}
            </li>
          )
        })}
      </ol>
      {!revealed && (
        <div className="order__bank" aria-label="Items to place">
          {bank.map((itemIndex, k) => (
            <button key={itemIndex} className="ordtile ordtile--bank" onClick={() => add(itemIndex)}>
              <kbd className="option__key">{k + 1}</kbd>
              {plain(step.items[itemIndex])}
            </button>
          ))}
        </div>
      )}
    </>
  )
}
