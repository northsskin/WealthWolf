import PenMark from '../PenMark.jsx'
import { Rich } from '../Rich.jsx'
import { plain } from '../../lib/content.js'
import { solutionText } from '../../lib/session.js'
import { feedbackTitle } from '../../lib/voiceLines.js'

const HINTS = {
  match: 'Tap a term, then its partner.',
  order: 'Tap items to place them in order. Tap again to remove.',
  number: 'Type your answer.',
  spot: 'Tap the line on the document.',
  sort: 'Tap the bucket each one belongs in.',
  allocate: 'Every dollar needs a job before you can check.',
}

// These finish on their own once everything is placed; there's nothing to check.
const SELF_CHECKING = new Set(['match', 'sort'])

export default function FeedbackBar({ phase, card, ready, correct, combo, mode, mistakes, strikes, seed, answer, onCheck, onNext }) {
  const { step } = card

  if (phase === 'feedback') {
    const tone = correct ? 'correct' : 'wrong'
    const title = feedbackTitle({ correct, mode, mistakes, strikes, seed })

    return (
      <footer className={`fb fb--${tone}`}>
        <div className="fb__inner">
          <div className="fb__message" role="status" aria-live="polite">
            <span className="fb__icon">
              {correct ? <PenMark kind="check" tone="green" delay={120} /> : <PenMark kind="cross" delay={120} />}
            </span>
            <div className="fb__text">
              <p className="fb__title">
                {title}
                {correct && combo >= 3 && (
                  <span className="fb__combo">
                    {combo} in a row
                  </span>
                )}
              </p>
              {!correct && step.type === 'order' && (
                <ol className="fb__sequence" aria-label="Correct order">
                  {step.items.map((item, i) => (
                    <li key={item}>
                      <span className="tabular">{i + 1}</span> {plain(item)}
                    </li>
                  ))}
                </ol>
              )}
              {!correct && !SELF_CHECKING.has(step.type) && step.type !== 'order' && (
                <p className="fb__solution">
                  Correct answer: <strong>{solutionText(step)}</strong>
                </p>
              )}
              {!correct && step.why?.[answer] && (
                <p className="fb__why">
                  <Rich text={step.why[answer]} />
                </p>
              )}
              {step.explain && (
                <p className="fb__explain">
                  <Rich text={step.explain} />
                </p>
              )}
            </div>
          </div>
          <button className={`btn fb__btn ${correct ? 'btn--green' : 'btn--danger'}`} onClick={onNext}>
            Continue
          </button>
        </div>
      </footer>
    )
  }

  if (step.type === 'info' || step.type === 'story') {
    return (
      <footer className="fb">
        <div className="fb__inner">
          <span />
          <button className="btn fb__btn" onClick={onNext}>
            Got it
          </button>
        </div>
      </footer>
    )
  }

  return (
    <footer className="fb">
      <div className="fb__inner">
        <p className="fb__hint">{HINTS[step.type] ?? ''}</p>
        {!SELF_CHECKING.has(step.type) && (
          <button className="btn fb__btn" onClick={onCheck} disabled={!ready}>
            Check
          </button>
        )}
      </div>
    </footer>
  )
}
