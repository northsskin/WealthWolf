import { useCallback, useEffect, useReducer, useRef, useState } from 'react'
import { Link, Navigate, useNavigate } from 'react-router'
import { BookA, Volume2, VolumeX, X } from 'lucide-react'
import FeedbackBar from '../components/lesson/FeedbackBar.jsx'
import { ReceiptLine, formatTime } from '../components/lesson/LessonComplete.jsx'
import { optionState, useDigitKeys } from '../components/lesson/steps/useDigitKeys.js'
import Stamp from '../components/Stamp.jsx'
import Term from '../components/Term.jsx'
import { UNLOCK_ALL, glossary } from '../lib/content.js'
import { dayKey } from '../lib/dates.js'
import { present } from '../lib/session.js'
import { sfx } from '../lib/sfx.js'
import { playVoice, stopVoice } from '../lib/voice.js'
import { barkKey, feedbackTitle } from '../lib/voiceLines.js'
import { buildDrill, wordStatus } from '../lib/words.js'
import { useAuth } from '../lib/auth.js'
import { actions, getState, useStore } from '../store/store.js'
import '../components/lesson/shared.css'
import '../components/lesson/LessonPlayer.css'
import '../components/lesson/LessonComplete.css'
import '../components/lesson/steps/steps.css'
import './WordDrill.css'

function init(cards) {
  return {
    queue: cards,
    total: cards.length,
    done: 0,
    answer: null,
    phase: 'answer', // answer → feedback → answer … → complete
    correct: null,
    answers: 0,
    mistakes: 0,
    combo: 0,
    firstTry: {}, // wordId -> right on the first try
    startedAt: Date.now(),
    endedAt: null,
  }
}

function reducer(state, action) {
  switch (action.type) {
    case 'answer':
      return state.phase === 'answer' ? { ...state, answer: action.value } : state
    case 'check': {
      const { wordId } = state.queue[0].step
      return {
        ...state,
        phase: 'feedback',
        correct: action.correct,
        answers: state.answers + 1,
        mistakes: state.mistakes + (action.correct ? 0 : 1),
        combo: action.correct ? state.combo + 1 : 0,
        firstTry: wordId in state.firstTry ? state.firstTry : { ...state.firstTry, [wordId]: action.correct },
        // A missed word comes back at the end, with its options reshuffled.
        queue: action.correct ? state.queue : [...state.queue, present(state.queue[0].step)],
      }
    }
    case 'next': {
      const queue = state.queue.slice(1)
      const done = state.done + (state.correct ? 1 : 0)
      if (!queue.length) return { ...state, queue, done, phase: 'complete', endedAt: action.now }
      return { ...state, queue, done, phase: 'answer', correct: null, answer: null }
    }
    default:
      return state
  }
}

// "Drill again" remounts the drill so it draws a fresh set of words.
export default function WordDrillScreen() {
  const [round, setRound] = useState(0)
  const { status } = useAuth()
  if (status === 'loading') return null
  if (status !== 'user' && !UNLOCK_ALL) return <Navigate to={`/signup?next=${encodeURIComponent('/glossary/drill')}`} replace />
  return <WordDrill key={round} onAgain={() => setRound((r) => r + 1)} />
}

function WordDrill({ onAgain }) {
  const navigate = useNavigate()
  const sound = useStore((s) => s.settings.sound)
  // Each word's status before this drill, to say which ones it locked in.
  const [before] = useState(() => {
    const { wordStats } = getState()
    return (id) => wordStatus(wordStats[id])
  })
  const [state, dispatch] = useReducer(reducer, null, () => {
    const { terms, wordStats } = getState()
    return init(buildDrill(terms, wordStats, dayKey()))
  })

  const card = state.queue[0]
  const ready = state.phase === 'answer' && state.answer !== null

  const check = useCallback(() => {
    if (!ready) return
    const correct = state.answer === card.step.answer
    actions.recordWord(card.step.wordId, correct)
    if (correct) sfx.correct()
    else sfx.wrong()
    const title = feedbackTitle({ correct, mode: 'review', seed: state.answers + 1 })
    playVoice(barkKey(title), { delay: 280 })
    dispatch({ type: 'check', correct })
  }, [ready, state.answer, state.answers, card])

  const next = useCallback(() => {
    if (state.queue.length === 1 && state.correct) sfx.complete()
    dispatch({ type: 'next', now: Date.now() })
  }, [state.queue.length, state.correct])

  const leave = useCallback(() => navigate('/glossary'), [navigate])

  // Enter drives the main button; Escape leaves (answers so far are already saved).
  const keys = useRef({})
  keys.current = { check, next, leave, phase: state.phase }
  useEffect(() => {
    function onKey(event) {
      const { check, next, leave, phase } = keys.current
      if (phase === 'complete') return
      if (event.key === 'Escape') return leave()
      if (event.key !== 'Enter' || event.repeat || event.target.closest?.('.term')) return
      event.preventDefault()
      if (phase === 'feedback') next()
      else check()
    }
    window.addEventListener('keydown', onKey)
    return () => window.removeEventListener('keydown', onKey)
  }, [])
  useEffect(() => {
    if (!sound) stopVoice()
  }, [sound])
  useEffect(() => stopVoice, [])

  useDigitKeys(card?.order.length ?? 0, (k) => dispatch({ type: 'answer', value: card.order[k] }), state.phase === 'answer')

  if (state.total === 0) return <Navigate to="/glossary" replace />
  if (state.phase === 'complete') return <DrillComplete state={state} before={before} onAgain={onAgain} />

  const { step } = card
  const progress = state.phase === 'feedback' && state.correct ? state.done + 1 : state.done
  const remaining = state.queue.length - (state.phase === 'feedback' && state.correct ? 1 : 0)
  const share = progress / (progress + remaining)

  return (
    <div className="player player--review">
      <header className="player__header">
        <button className="player__icon-btn" onClick={leave} aria-label="Leave the drill">
          <X />
        </button>
        <div className="player__progress-wrap">
          {state.combo >= 3 && (
            <span key={state.combo} className="player__combo">
              {state.combo} in a row
            </span>
          )}
          <div
            className="player__progress"
            role="progressbar"
            aria-label="Drill progress"
            aria-valuemin={0}
            aria-valuemax={100}
            aria-valuenow={Math.round(share * 100)}
          >
            <span style={{ width: `${Math.max(share * 100, 3)}%` }} />
          </div>
        </div>
        <button
          className="player__icon-btn player__sound"
          onClick={() => actions.setSound(!sound)}
          aria-label={sound ? 'Mute sounds' : 'Unmute sounds'}
          aria-pressed={!sound}
        >
          {sound ? <Volume2 /> : <VolumeX />}
        </button>
      </header>

      <main className="player__main">
        <div className="step" key={card.key}>
          <p className="step__label">
            <BookA /> Word drill
          </p>
          <h2 className="step__prompt">{step.prompt}</h2>
          <p className={`cue cue--${step.cueKind}`}>{step.cue}</p>
          <div className={`choices choices--${step.cueKind}`} role="radiogroup" aria-label="Answers">
            {card.order.map((choiceIndex, k) => (
              <button
                key={choiceIndex}
                role="radio"
                aria-checked={state.answer === choiceIndex}
                className={`option ${optionState({ value: choiceIndex, picked: state.answer, answer: step.answer, revealed: state.phase === 'feedback' })}`}
                onClick={() => dispatch({ type: 'answer', value: choiceIndex })}
                disabled={state.phase === 'feedback'}
              >
                <kbd className="option__key">{k + 1}</kbd>
                <span>{step.choices[choiceIndex]}</span>
              </button>
            ))}
          </div>
        </div>
      </main>

      <FeedbackBar
        phase={state.phase}
        card={card}
        ready={ready}
        correct={state.correct}
        combo={state.combo}
        mode="review"
        seed={state.answers}
        answer={state.answer}
        onCheck={check}
        onNext={next}
      />
    </div>
  )
}

function DrillComplete({ state, before, onAgain }) {
  const words = Object.keys(state.firstTry)
  const missed = words.filter((id) => !state.firstTry[id])
  const right = words.length - missed.length
  const { wordStats } = getState()
  const lockedIn = words.filter((id) => before(id) !== 'solid' && wordStatus(wordStats[id]) === 'solid')
  const perfect = missed.length === 0
  const seconds = Math.round((state.endedAt - state.startedAt) / 1000)

  return (
    <div className="done">
      <main className="done__main">
        <section className="receipt" aria-labelledby="drill-title">
          <header className="receipt__head">
            <p className="eyebrow">Word drill receipt</p>
            <h1 id="drill-title" className="display done__title">
              {perfect ? 'Every word, first try.' : 'Drill done.'}
            </h1>
            <p className="done__sub">
              {perfect
                ? 'Nothing for the Wolf to mark.'
                : `${missed.length === 1 ? 'One word' : `${missed.length} words`} to keep an eye on. ${missed.length === 1 ? 'It comes' : 'They come'} up first next drill.`}
            </p>
          </header>

          <dl className="receipt__lines">
            <ReceiptLine label="Words drilled" value={words.length} />
            <ReceiptLine label="Missed" value={missed.length} />
            <ReceiptLine label="Time" value={formatTime(seconds)} />
          </dl>

          <p className="receipt__total">
            <span>Right first time</span>
            <span className="figure">
              {right} / {words.length}
            </span>
          </p>

          {missed.length > 0 && <WordChips title="Shaky" ids={missed} />}
          {lockedIn.length > 0 && <WordChips title="Now solid" ids={lockedIn} />}

          <Stamp
            text={perfect ? 'Word perfect · Word perfect · ' : 'Drilled · Drilled · Drilled · '}
            tone="gold"
            className="receipt__stamp"
            delay={500}
            tilt={-12}
          />
        </section>
      </main>

      <footer className="fb">
        <div className="fb__inner drill__actions">
          <Link to="/glossary" className="btn btn--ghost fb__btn">
            Glossary
          </Link>
          <button className="btn fb__btn" onClick={onAgain} autoFocus>
            Drill again
          </button>
        </div>
      </footer>
    </div>
  )
}

function WordChips({ title, ids }) {
  return (
    <div className="receipt__words">
      <p className="eyebrow">{title}</p>
      <div className="receipt__words-list">
        {ids.map((id) => (
          <Term key={id} id={id} chip>
            {glossary[id].term}
          </Term>
        ))}
      </div>
    </div>
  )
}
