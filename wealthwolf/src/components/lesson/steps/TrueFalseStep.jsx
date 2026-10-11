import { Check, X } from 'lucide-react'
import { Rich } from '../../Rich.jsx'
import { optionState, useDigitKeys } from './useDigitKeys.js'

const OPTIONS = [
  { value: true, label: 'True', Icon: Check },
  { value: false, label: 'False', Icon: X },
]

export default function TrueFalseStep({ card, answer, setAnswer, revealed }) {
  const { step } = card
  useDigitKeys(2, (k) => setAnswer(OPTIONS[k].value), !revealed)

  return (
    <>
      <blockquote className="statement">
        <Rich text={step.prompt} />
      </blockquote>
      <div className="tf" role="radiogroup" aria-label="True or false">
        {OPTIONS.map(({ value, label, Icon }, k) => (
          <button
            key={label}
            role="radio"
            aria-checked={answer === value}
            className={`option tf__option ${optionState({ value, picked: answer, answer: step.answer, revealed })}`}
            onClick={() => setAnswer(value)}
            disabled={revealed}
          >
            <kbd className="option__key">{k + 1}</kbd>
            <Icon />
            <span>{label}</span>
          </button>
        ))}
      </div>
    </>
  )
}
