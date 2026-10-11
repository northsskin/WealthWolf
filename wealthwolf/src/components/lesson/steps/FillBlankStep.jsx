import { Rich } from '../../Rich.jsx'
import { plain } from '../../../lib/content.js'
import { useDigitKeys } from './useDigitKeys.js'

export default function FillBlankStep({ card, answer, setAnswer, revealed, correct }) {
  const { step, order } = card
  const [before, after] = step.prompt.split('___')
  const filled = answer !== null
  useDigitKeys(order.length, (k) => setAnswer(order[k]), !revealed)

  let slotState = filled ? 'is-filled' : ''
  if (revealed) slotState = correct ? 'is-correct' : 'is-wrong'

  return (
    <>
      <p className="fill__sentence">
        <Rich text={before} />
        <button
          className={`fill__slot ${slotState}`}
          onClick={() => setAnswer(null)}
          disabled={!filled || revealed}
          aria-label={filled ? `Selected: ${plain(step.choices[answer])}. Tap to clear.` : 'Empty gap'}
        >
          {filled ? plain(step.choices[answer]) : ' '}
        </button>
        <Rich text={after} />
      </p>
      <div className="fill__bank" aria-label="Word choices">
        {order.map((choiceIndex, k) => (
          <button
            key={choiceIndex}
            className={answer === choiceIndex ? 'wordchip is-used' : 'wordchip'}
            onClick={() => setAnswer(choiceIndex)}
            disabled={revealed || answer === choiceIndex}
            aria-keyshortcuts={String(k + 1)}
          >
            {plain(step.choices[choiceIndex])}
          </button>
        ))}
      </div>
    </>
  )
}
