import { Rich } from '../../Rich.jsx'
import { plain } from '../../../lib/content.js'
import { optionState, useDigitKeys } from './useDigitKeys.js'

export default function ChoiceStep({ card, answer, setAnswer, revealed }) {
  const { step, order } = card
  useDigitKeys(order.length, (k) => setAnswer(order[k]), !revealed)

  return (
    <>
      <h2 className="step__prompt">
        <Rich text={step.prompt} />
      </h2>
      <div className="choices" role="radiogroup" aria-label="Answers">
        {order.map((choiceIndex, k) => (
          <button
            key={choiceIndex}
            role="radio"
            aria-checked={answer === choiceIndex}
            className={`option ${optionState({ value: choiceIndex, picked: answer, answer: step.answer, revealed })}`}
            onClick={() => setAnswer(choiceIndex)}
            disabled={revealed}
          >
            <kbd className="option__key">{k + 1}</kbd>
            <span>{plain(step.choices[choiceIndex])}</span>
          </button>
        ))}
      </div>
    </>
  )
}
