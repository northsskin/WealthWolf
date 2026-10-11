import { useEffect, useState } from 'react'
import { Link } from 'react-router'
import Stamp from '../Stamp.jsx'
import Term from '../Term.jsx'
import { glossary } from '../../lib/content.js'
import { rankForXp } from '../../lib/ranks.js'
import './shared.css'
import './LessonComplete.css'

const reducedMotion = () => window.matchMedia?.('(prefers-reduced-motion: reduce)').matches

function useCountUp(target, duration = 900, delay = 300) {
  const [value, setValue] = useState(() => (reducedMotion() ? target : 0))
  useEffect(() => {
    if (reducedMotion()) return
    let frame
    let start
    const timer = setTimeout(() => {
      const tick = (now) => {
        start ??= now
        const t = Math.min((now - start) / duration, 1)
        setValue(Math.round(target * (1 - (1 - t) ** 3)))
        if (t < 1) frame = requestAnimationFrame(tick)
      }
      frame = requestAnimationFrame(tick)
    }, delay)
    return () => {
      clearTimeout(timer)
      cancelAnimationFrame(frame)
    }
  }, [target, duration, delay])
  return value
}

export function formatTime(seconds) {
  return `${Math.floor(seconds / 60)}:${String(seconds % 60).padStart(2, '0')}`
}

function RankMeter({ xpBefore, xpAfter, rankedUp }) {
  const before = rankForXp(xpBefore)
  const after = rankForXp(xpAfter)
  const [fill, setFill] = useState(rankedUp ? 0 : before.progress)

  useEffect(() => {
    const timer = setTimeout(() => setFill(after.progress), 450)
    return () => clearTimeout(timer)
  }, [after.progress])

  return (
    <div className="meter">
      <div className="meter__labels">
        <span className="meter__rank">{after.rank.name}</span>
        <span className="tabular">{after.next ? `${after.xpToNext} XP to ${after.next.name}` : 'Top of the pack'}</span>
      </div>
      <div className="meter__bar">
        <span style={{ width: `${fill * 100}%` }} />
      </div>
    </div>
  )
}

const COPY = {
  boss: { title: 'Trial passed.', sub: 'The den respects you.', stamp: 'Trial passed', kind: 'Den Trial' },
  section: { title: 'Section cleared.', sub: 'Every unit, one sitting, three strikes allowed. The next section is open.', stamp: 'Section cleared', kind: 'Section Trial' },
  review: { title: 'Memory sharpened.', sub: 'What you nearly forgot is locked back in.', stamp: 'Reviewed', kind: 'Review' },
  perfect: { title: 'Flawless.', sub: 'Zero mistakes. Nothing for the Wolf to mark.', stamp: 'Paid in full', kind: 'Lesson' },
  lesson: { title: 'Lesson cleared.', sub: 'Mistakes and all. That\u2019s how it sticks.', stamp: 'Lesson cleared', kind: 'Lesson' },
}

// One line of the receipt: label, dotted leader, figure.
export function ReceiptLine({ label, value, note }) {
  return (
    <div className="receipt__line">
      <dt>{label}</dt>
      <dd>
        <span className="figure">{value}</span>
        {note && <span className="receipt__note">{note}</span>}
      </dd>
    </div>
  )
}

export default function LessonComplete({ mode, result, stats, learnedTerms = [], guest = false, onContinue, onSave }) {
  const perfect = stats.mistakes === 0
  const xp = useCountUp(result.xpGained)
  const copy = COPY[mode === 'lesson' && perfect ? 'perfect' : mode] ?? COPY.lesson
  const streakNote = result.streakExtended ? (result.streak > 1 ? 'Extended. Keep it alive.' : 'Started. Come back tomorrow.') : 'Already safe for today.'

  return (
    <div className="done">
      <main className="done__main">
        <section className="receipt" aria-labelledby="receipt-title">
          <header className="receipt__head">
            <p className="eyebrow">{copy.kind} receipt</p>
            <h1 id="receipt-title" className="display done__title">
              {copy.title}
            </h1>
            <p className="done__sub">{copy.sub}</p>
          </header>

          <dl className="receipt__lines">
            {result.breakdown.map((item) => (
              <ReceiptLine key={item.label} label={item.label} value={`+${item.xp} XP`} />
            ))}
            <ReceiptLine label="Accuracy" value={`${stats.accuracy}%`} />
            <ReceiptLine label="Time" value={formatTime(stats.seconds)} />
            {stats.bestCombo >= 3 && <ReceiptLine label="Best run" value={`${stats.bestCombo} in a row`} />}
            <ReceiptLine label="Streak" value={`${result.streak} day${result.streak === 1 ? '' : 's'}`} note={streakNote} />
          </dl>

          <p className="receipt__total">
            <span>Total</span>
            <span className="figure">+{xp} XP</span>
          </p>

          {guest && (
            <p className="receipt__unsaved">
              <strong>Not saved yet.</strong> This lives only in this browser. Create a free account to keep it and
              unlock the rest of the path.
            </p>
          )}

          {learnedTerms.length > 0 && (
            <div className="receipt__words">
              <div className="receipt__words-head">
                <p className="eyebrow">New words learned</p>
                <Link to="/glossary" className="receipt__words-link">
                  In your glossary
                </Link>
              </div>
              <div className="receipt__words-list">
                {learnedTerms.map((id) => (
                  <Term key={id} id={id} chip>
                    {glossary[id].term}
                  </Term>
                ))}
              </div>
            </div>
          )}

          <Stamp text={`${copy.stamp} \u00b7 ${copy.stamp} \u00b7 `} tone="gold" className="receipt__stamp" delay={500} tilt={-12} />
        </section>

        <RankMeter xpBefore={result.xpBefore} xpAfter={result.xpAfter} rankedUp={Boolean(result.rankUp)} />

        {result.rankUp && (
          <div className="done__rankup">
            <span className="done__rankup-badge" aria-hidden="true">
              {result.rankUp.name[0]}
            </span>
            <p>
              <strong>Rank up. You’re a {result.rankUp.name} now.</strong> {result.rankUp.tagline}
            </p>
          </div>
        )}
      </main>

      <footer className="fb">
        <div className={guest ? 'fb__inner done__actions' : 'fb__inner'}>
          {guest ? (
            <>
              <button className="btn btn--ghost fb__btn" onClick={onContinue}>
                Later
              </button>
              <button className="btn fb__btn" onClick={onSave} autoFocus>
                Save my progress
              </button>
            </>
          ) : (
            <>
              <span />
              <button className="btn fb__btn" onClick={onContinue} autoFocus>
                Continue
              </button>
            </>
          )}
        </div>
      </footer>
    </div>
  )
}
