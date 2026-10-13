import { useEffect, useRef, useState } from 'react'
import { Link, useNavigate } from 'react-router'
import { ArrowRight } from 'lucide-react'
import Bar from '../components/Bar.jsx'
import PenMark from '../components/PenMark.jsx'
import Stamp from '../components/Stamp.jsx'
import ThemeToggle from '../components/ThemeToggle.jsx'
import WolfMark from '../components/WolfMark.jsx'
import AccountMenu from '../components/AccountMenu.jsx'
import { useAuth } from '../lib/auth.js'
import { actions, useStore } from '../store/store.js'
import { RANKS } from '../lib/ranks.js'
import { glossary, lessons, modules } from '../lib/content.js'
import { formatNumber } from '../lib/session.js'
import '../components/lesson/steps/steps.css'
import './Landing.css'

// One ordinary month, as the Wolf would audit it. Figures add up:
// 2,400 in, 1,811 out, 589 left over, 0 saved.
const MONTH = [
  { entry: 'Paycheck', in: 2400 },
  { entry: 'Rent', out: 1100 },
  { entry: 'Phone and internet', out: 95 },
  { entry: 'Groceries', out: 260 },
  { entry: 'Takeout, 14 times', out: 310, mark: 'circle', note: 'Fourteen? Cook twice a week and this halves.' },
  { entry: 'Subscriptions (4)', out: 46, mark: 'strike', note: 'You use one of these. Cancel three.' },
  { entry: 'Savings', out: 0, mark: 'underline', note: '$589 left over and none of it saved. Fix this first.' },
]
// The closing line counts the real course, so it stays true as lessons are added.
const CLOSING = `${modules.length} units. ${lessons.filter((l) => l.type === 'lesson').length} lessons. ${Object.keys(glossary).length} new words. One wolf checking your work.`

const LEFT_OVER = MONTH.reduce((sum, row) => sum + (row.in ?? 0) - (row.out ?? 0), 0)
const PEN_START = 350 // a beat after the ledger scrolls into view
const PEN_GAP = 650

const CONTENTS = [
  {
    title: 'Bite-Sized Lessons',
    body: 'One idea per lesson, then the real thing: pay stubs to read, bills to check, a month of someone else’s money to sort out. Every new word is explained the moment it shows up.',
    figure: '5 min',
  },
  {
    title: 'Portfolio Simulator',
    body: 'Invest pretend money and fast-forward thirty years. Make the expensive mistakes here, not with your rent.',
    figure: '30 yrs',
    note: 'Opening soon.',
  },
  {
    title: 'Smart Repetition',
    body: "The questions you got wrong come back, right before you'd forget them. You don't choose what to review. The Wolf does.",
    figure: '8 / review',
  },
  {
    title: 'Earn Your Rank',
    body: 'Every lesson pays XP. Enough of it moves you up a rank. Miss a day and your streak starts again from one.',
    figure: '5 ranks',
  },
]

const RANK_SKILLS = {
  pup: 'Tell income from expenses, and say where last month went.',
  scout: 'Build a budget that survives an actual month.',
  hunter: 'Keep a cushion for surprises and pay yourself first.',
  wolf: 'Run a whole month on a plan: bills, savings and goals.',
  alpha: 'Hold the long plan: a safety net, investments, retirement, and a will.',
}

// True once the first row the Wolf marks is fully on screen. The markup plays
// from that moment, so on a phone it happens when you get there, not before.
function useSeen(ref, selector) {
  const [seen, setSeen] = useState(false)
  useEffect(() => {
    const target = ref.current?.querySelector(selector) ?? ref.current
    if (!target || seen) return
    if (!('IntersectionObserver' in window)) return setSeen(true)
    const io = new IntersectionObserver(([entry]) => entry.isIntersecting && setSeen(true), { threshold: 1 })
    // Wait for the web fonts: before they land, the headline sets in a wider
    // fallback face and the ledger can briefly sit higher on the page.
    let cancelled = false
    document.fonts.ready.then(() => !cancelled && io.observe(target))
    return () => {
      cancelled = true
      io.disconnect()
    }
  }, [ref, selector, seen])
  return seen
}

export default function Landing() {
  const navigate = useNavigate()
  const started = useStore((s) => s.startedAt !== null)
  const { status: authStatus } = useAuth()
  const auditRef = useRef(null)
  const auditSeen = useSeen(auditRef, '.audit__row.is-marked')

  function start() {
    actions.startLearning()
    navigate('/learn')
  }

  return (
    <div className="landing">
      <Bar>
        {authStatus === 'guest' && (
          <Link to="/signin" className="bar__signin">
            Sign in
          </Link>
        )}
        {authStatus === 'user' ? <AccountMenu /> : <ThemeToggle />}
        {started ? (
          <Link to="/learn" className="btn btn--ghost bar__cta">
            Continue <ArrowRight />
          </Link>
        ) : (
          <button className="btn bar__cta" onClick={start}>
            Start free
          </button>
        )}
      </Bar>

      <main>
        <section className="sheet" aria-labelledby="hero-title">
          <div className="sheet__head">
            <p className="eyebrow sheet__kicker">Money lessons for people who were never taught</p>
            <h1 id="hero-title" className="display hero__title">
              Your portfolio won't build itself.
            </h1>
            <div className="hero__pitch">
              <p className="hero__sub">
                Master personal finance through gamified lessons, real-world simulations, and a Wolf who
                won't let you slack off.
              </p>
              <div className="hero__cta">
                <button className="btn btn--lg" onClick={start}>
                  Start Learning Free
                </button>
                <p className="figure hero__fine">Free. Lesson one needs no account. Five minutes a day.</p>
              </div>
            </div>
          </div>

          <div
            ref={auditRef}
            className={auditSeen ? 'audit is-live' : 'audit'}
            role="table"
            aria-label="An ordinary month, audited by the Wolf"
          >
            <div className="audit__row audit__row--head" role="row">
              <span role="columnheader" className="audit__no">No.</span>
              <span role="columnheader">This month</span>
              <span role="columnheader" className="audit__fig">In</span>
              <span role="columnheader" className="audit__fig">Out</span>
              <span role="columnheader" className="audit__note">The Wolf's notes</span>
            </div>

            {MONTH.map((row, i) => {
              const order = MONTH.slice(0, i).filter((r) => r.mark).length
              const delay = PEN_START + order * PEN_GAP
              return (
                <div key={row.entry} className={`audit__row${row.mark ? ' is-marked' : ''}`} role="row">
                  <span role="cell" className="audit__no figure">
                    {String(i + 1).padStart(2, '0')}
                  </span>
                  <span role="cell" className="audit__entry">
                    <span className="audit__entry-text">
                      {row.entry}
                      {row.mark === 'strike' && <PenMark kind="strike" delay={delay} className="audit__strike" />}
                    </span>
                  </span>
                  <span role="cell" className="audit__fig figure" data-sign="+">
                    {row.in !== undefined && formatNumber(row.in)}
                  </span>
                  <span role="cell" className="audit__fig figure" data-sign="−">
                    {row.out !== undefined && (
                      <span className="audit__amount">
                        {formatNumber(row.out)}
                        {row.mark === 'circle' && <PenMark kind="circle" delay={delay} className="audit__circle" />}
                        {row.mark === 'underline' && (
                          <PenMark kind="underline" delay={delay} className="audit__underline" />
                        )}
                      </span>
                    )}
                  </span>
                  <span role="cell" className="audit__note">
                    {row.note && (
                      <span className="audit__note-text" style={{ '--pen-delay': `${delay + 250}ms` }}>
                        {row.note}
                      </span>
                    )}
                  </span>
                </div>
              )
            })}

            <div className="audit__row audit__row--total" role="row">
              <span role="cell" className="audit__no" />
              <span role="cell" className="audit__entry">
                Left over
              </span>
              <span role="cell" className="audit__fig figure">
                {formatNumber(LEFT_OVER)}
              </span>
              <span role="cell" className="audit__fig" />
              <span role="cell" className="audit__note" />
            </div>

            <Stamp text="Audited by the Wolf · Audited by the Wolf ·" className="audit__stamp" delay={PEN_START + 3 * PEN_GAP + 300} />
          </div>
        </section>

        <TryOne onStart={start} />

        <section className="part" aria-labelledby="contents-title">
          <SectionHead no="03" id="contents-title" title="What's in the book" />
          <ol className="contents">
            {CONTENTS.map((item, i) => (
              <li key={item.title} className="contents__row">
                <span className="figure contents__no">{String(i + 1).padStart(2, '0')}</span>
                <div className="contents__main">
                  <h3 className="display contents__title">{item.title}</h3>
                  <p className="contents__body">{item.body}</p>
                  {item.note && <p className="contents__note">{item.note}</p>}
                </div>
                <span className="figure contents__figure">{item.figure}</span>
              </li>
            ))}
          </ol>
        </section>

        <section className="part" aria-labelledby="ladder-title">
          <SectionHead no="04" id="ladder-title" title="The ladder" aside="XP to reach it" />
          <ol className="ladder">
            {RANKS.map((rank) => (
              <li key={rank.id} className={`ladder__row ladder__row--${rank.id}`}>
                <span className="ladder__badge" aria-hidden="true">
                  {rank.name[0]}
                </span>
                <div className="ladder__main">
                  <h3 className="display ladder__name">{rank.name}</h3>
                  <p className="ladder__skill">{RANK_SKILLS[rank.id]}</p>
                </div>
                <span className="figure ladder__xp">{formatNumber(rank.minXp)}</span>
              </li>
            ))}
          </ol>
        </section>

        <section className="close" aria-labelledby="close-title">
          <h2 id="close-title" className="display close__title">
            {CLOSING}
          </h2>
          <div className="close__cta">
            <button className="btn btn--lg" onClick={start}>
              Start Learning Free
            </button>
            <p className="figure hero__fine">Starts with what income actually is.</p>
          </div>
        </section>
      </main>

      <footer className="landing__footer">
        <WolfMark size="xs" />
        <span className="figure">Wealthwolf prototype. Educational content, not financial advice.</span>
      </footer>
    </div>
  )
}

function SectionHead({ no, id, title, aside }) {
  return (
    <header className="part__head">
      <span className="figure part__no">{no}</span>
      <h2 id={id} className="display part__title">
        {title}
      </h2>
      {aside && <span className="eyebrow part__aside">{aside}</span>}
    </header>
  )
}

// A real question from lesson one, answerable right here.
const TRY = {
  context: 'Take your expenses away from your income and you get your cash flow: what’s left over.',
  prompt: 'You earn $3,200 a month and spend $2,900. What’s your cash flow?',
  choices: ['$6,100', '$300', '−$300'],
  answer: 1,
}

function TryOne({ onStart }) {
  const [picked, setPicked] = useState(null)
  const answered = picked !== null
  const correct = picked === TRY.answer

  return (
    <section className="part" aria-labelledby="try-title">
      <SectionHead no="02" id="try-title" title="Try a question from lesson one" />
      <div className="try">
        <div className="scenario">
          <WolfMark size="md" />
          <p>{TRY.context}</p>
        </div>
        <p className="try__prompt">{TRY.prompt}</p>
        <div className="try__choices" role="radiogroup" aria-label="Answers">
          {TRY.choices.map((choice, i) => {
            let state = ''
            if (answered && i === TRY.answer) state = 'is-correct'
            else if (answered && i === picked) state = 'is-wrong'
            else if (answered) state = 'is-dim'
            return (
              <button
                key={choice}
                role="radio"
                aria-checked={picked === i}
                className={`option try__option ${state}`}
                onClick={() => setPicked(i)}
                disabled={answered}
              >
                <span className="figure try__figure">{choice}</span>
                {answered && i === TRY.answer && <PenMark kind="check" tone="green" className="try__mark" />}
                {answered && i === picked && !correct && <PenMark kind="cross" className="try__mark" />}
              </button>
            )
          })}
        </div>
        <div className="try__result" aria-live="polite">
          {answered && (
            <>
              <p className={correct ? 'try__verdict is-correct' : 'try__verdict is-wrong'}>
                {correct ? 'That’s it.' : 'Not quite.'} <span>$3,200 − $2,900 = $300 left over.</span>
              </p>
              <p className="try__next">
                {correct
                  ? 'That was question four of lesson one. The whole lesson takes about five minutes.'
                  : 'That’s exactly what lesson one covers, in about five minutes.'}
              </p>
              <button className="btn" onClick={onStart}>
                Start lesson one
              </button>
            </>
          )}
        </div>
      </div>
    </section>
  )
}
