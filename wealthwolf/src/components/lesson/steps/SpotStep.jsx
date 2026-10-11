import { Rich } from '../../Rich.jsx'
import Document from '../Document.jsx'

export default function SpotStep({ card, answer, setAnswer, revealed }) {
  const { step } = card
  return (
    <>
      <h2 className="step__prompt">
        <Rich text={step.prompt} />
      </h2>
      <div className="spot">
        <Document doc={step.doc} interactive picked={answer} revealed={revealed} answer={step.answer} onPick={setAnswer} />
      </div>
    </>
  )
}
