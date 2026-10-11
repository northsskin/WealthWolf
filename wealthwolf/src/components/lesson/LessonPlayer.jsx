import { useCallback, useEffect, useMemo, useReducer, useRef, useState } from 'react'
import { useNavigate } from 'react-router'
import {
  BookOpen,
  Calculator,
  Heart,
  HeartCrack,
  Link2,
  ListChecks,
  ListOrdered,
  MessageSquareText,
  ReceiptText,
  Scale,
  ScanSearch,
  Shapes,
  Wallet,
  TextCursorInput,
  Volume2,
  VolumeX,
  X,
} from 'lucide-react'
import FeedbackBar from './FeedbackBar.jsx'
import Term, { TermContext } from '../Term.jsx'
import { Rich } from '../Rich.jsx'
import WolfMark from '../WolfMark.jsx'
import Dialog from './Dialog.jsx'
import LessonComplete from './LessonComplete.jsx'
import TrialFailed from './TrialFailed.jsx'
import InfoStep from './steps/InfoStep.jsx'
import ChoiceStep from './steps/ChoiceStep.jsx'
import TrueFalseStep from './steps/TrueFalseStep.jsx'
import FillBlankStep from './steps/FillBlankStep.jsx'
import NumberStep from './steps/NumberStep.jsx'
import OrderStep from './steps/OrderStep.jsx'
import MatchStep from './steps/MatchStep.jsx'
import SpotStep from './steps/SpotStep.jsx'
import SortStep from './steps/SortStep.jsx'
import AllocateStep from './steps/AllocateStep.jsx'
import StoryStep, { StoryRecall } from './steps/StoryStep.jsx'
import { Documents } from './Document.jsx'
import CalculatorPanel, { CalculatorTab } from './Calculator.jsx'
import { BOSS_STRIKES, buildSession, grade, initialAnswer, isReady, present } from '../../lib/session.js'
import { getLesson, glossary, stepDocs, stepTerms } from '../../lib/content.js'
import { sfx } from '../../lib/sfx.js'
import { hasVoice, playVoice, stopVoice } from '../../lib/voice.js'
import { barkKey, feedbackTitle } from '../../lib/voiceLines.js'
import { actions, getState, MAX_HEARTS, useStore } from '../../store/store.js'
import { useAuth } from '../../lib/auth.js'
import './shared.css'
import './LessonPlayer.css'
import './steps/steps.css'

const STEP_UI = {
  info: { Component: InfoStep, label: 'New idea', Icon: BookOpen },
  multiple_choice: { Component: ChoiceStep, label: 'Choose the answer', Icon: ListChecks },
  true_false: { Component: TrueFalseStep, label: 'True or false', Icon: Scale },
  fill_blank: { Component: FillBlankStep, label: 'Fill the gap', Icon: TextCursorInput },
  number: { Component: NumberStep, label: 'Run the numbers', Icon: Calculator },
  order: { Component: OrderStep, label: 'Put it in order', Icon: ListOrdered },
  match: { Component: MatchStep, label: 'Match the pairs', Icon: Link2 },
  story: { Component: StoryStep, label: 'Money story', Icon: MessageSquareText },
  spot: { Component: SpotStep, label: 'Spot the problem', Icon: ScanSearch },
  sort: { Component: SortStep, label: 'Sort it', Icon: Shapes },
  allocate: { Component: AllocateStep, label: 'Build the budget', Icon: Wallet },
}

// Cards you read rather than answer: they advance with "Got it".
export const READING_TYPES = new Set(['info', 'story'])

// A question with a document attached gets a label that says so; two side by
// side means you're comparing offers.
const DOC_LABEL = { label: 'Read the document', Icon: ReceiptText }
const COMPARE_LABEL = { label: 'Make the call', Icon: Scale }


function init(session) {
  return {
    mode: session.mode,
    queue: session.cards, // queue[0] is on screen
    done: 0,
    answer: initialAnswer(session.cards[0]),
    phase: 'answer', // answer → feedback → answer … → complete | failed
    correct: null,
    answers: 0,
    rightAnswers: 0,
    mistakes: 0,
    combo: 0,
    bestCombo: 0,
    startedAt: Date.now(),
    endedAt: null,
  }
}

function reducer(state, action) {
  switch (action.type) {
    case 'answer': {
      if (state.phase !== 'answer') return state
      // Steps may pass an updater, so quick repeated taps each build on the last.
      const answer = typeof action.value === 'function' ? action.value(state.answer) : action.value
      return { ...state, answer }
    }

    case 'check': {
      const combo = action.correct ? state.combo + 1 : 0
      return {
        ...state,
        phase: 'feedback',
        correct: action.correct,
        answers: state.answers + 1,
        rightAnswers: state.rightAnswers + (action.correct ? 1 : 0),
        mistakes: state.mistakes + (action.correct ? 0 : 1),
        combo,
        bestCombo: Math.max(state.bestCombo, combo),
        // Missed questions come back at the end until you get them right.
        queue: action.retry ? [...state.queue, action.retry] : state.queue,
      }
    }

    case 'next': {
      const cleared = state.phase === 'answer' || state.correct || state.mode === 'boss'
      const queue = state.queue.slice(1)
      const done = state.done + (cleared ? 1 : 0)
      if (state.mode === 'boss' && state.mistakes >= BOSS_STRIKES) {
        return { ...state, queue, done, phase: 'failed', endedAt: action.now }
      }
      if (queue.length === 0) return { ...state, queue, done, phase: 'complete', endedAt: action.now }
      return { ...state, queue, done, phase: 'answer', correct: null, answer: initialAnswer(queue[0]) }
    }

    default:
      return state
  }
}

function progressOf(state) {
  if (state.phase === 'complete') return 1
  if (state.phase === 'feedback') {
    const counted = state.correct || state.mode === 'boss' ? 1 : 0
    const remaining = state.queue.length - 1
    return (state.done + counted) / (state.done + counted + remaining)
  }
  return state.done / (state.done + state.queue.length)
}

export default function LessonPlayer({ lesson, onRestart }) {
  const navigate = useNavigate()
  const hearts = useStore((s) => s.hearts)
  const sound = useStore((s) => s.settings.sound)
  const { status: authStatus } = useAuth()
  const [state, dispatch] = useReducer(reducer, null, () => init(buildSession(lesson, getState())))
  const [result, setResult] = useState(null)
  const [quitting, setQuitting] = useState(false)
  const [calcOpen, setCalcOpen] = useState(false)

  // Words the learner hadn't met when this session started stay "new" for the
  // whole session, so a re-queued question still highlights them.
  const [unknownTerms] = useState(() => new Set(Object.keys(glossary).filter((id) => !getState().terms[id])))
  const termContext = useMemo(() => ({ isNew: (id) => unknownTerms.has(id) }), [unknownTerms])
  const metTerms = useRef(new Set())

  const card = state.queue[0]
  const outOfHearts = hearts === 0 && state.phase === 'answer'
  const ready = card && state.phase === 'answer' && isReady(card, state.answer)

  // The Wolf calls the verdict out loud, a beat after the chime.
  const bark = useCallback(
    (correct, mistakes) => {
      const title = feedbackTitle({ correct, mode: state.mode, mistakes, strikes: BOSS_STRIKES, seed: state.answers + 1 })
      playVoice(barkKey(title), { delay: 280 })
    },
    [state.mode, state.answers],
  )

  const check = useCallback(() => {
    if (!ready) return
    const correct = grade(card, state.answer)
    actions.recordAnswer(card.step.id, correct)
    if (correct) sfx.correct()
    else {
      sfx.wrong()
      actions.loseHeart()
    }
    bark(correct, state.mistakes + (correct ? 0 : 1))
    dispatch({ type: 'check', correct, retry: !correct && state.mode !== 'boss' ? present(card.step) : null })
  }, [ready, card, state.answer, state.mode, bark])

  const next = useCallback(() => {
    const met = stepTerms(state.queue[0].step)
    met.forEach((id) => metTerms.current.add(id))
    actions.learnTerms(met)
    const failed = state.mode === 'boss' && state.mistakes >= BOSS_STRIKES
    const finishing = !failed && state.queue.length === 1 && (state.phase === 'answer' || state.correct || state.mode === 'boss')
    if (failed) sfx.fail()
    if (finishing) {
      setResult(actions.completeLesson(lesson, { perfect: state.mistakes === 0 }))
      sfx.complete()
    }
    dispatch({ type: 'next', now: Date.now() })
  }, [lesson, state])

  const solvedOnItsOwn = useCallback(
    (misses) => {
      actions.recordAnswer(card.step.id, misses === 0)
      sfx.correct()
      bark(true, state.mistakes)
      dispatch({ type: 'check', correct: true, retry: null })
    },
    [card, bark, state.mistakes],
  )

  // Read each card aloud as it appears (concept cards, stories, the Wolf's bubble).
  useEffect(() => {
    if (card && state.phase === 'answer' && hasVoice(card.step.id)) playVoice(card.step.id, { delay: 250 })
  }, [card?.key]) // eslint-disable-line react-hooks/exhaustive-deps
  useEffect(() => {
    if (!sound) stopVoice()
  }, [sound])
  useEffect(() => stopVoice, [])

  const quit = useCallback(() => {
    if (state.done === 0 && state.answers === 0) navigate('/learn')
    else setQuitting(true)
  }, [state.done, state.answers, navigate])

  // Enter drives the primary button; Escape asks to quit.
  const keys = useRef({})
  keys.current = { check, next, quit, state, ready, blocked: quitting || outOfHearts }
  useEffect(() => {
    function onKey(event) {
      const { check, next, quit, state, ready, blocked } = keys.current
      if (blocked || state.phase === 'complete' || state.phase === 'failed') return
      if (event.key === 'Escape') return quit()
      if (event.key !== 'Enter' || event.repeat) return
      if (event.target.closest?.('.term, .recall')) return // let Enter open a definition or the story
      event.preventDefault()
      if (state.phase === 'feedback') next()
      else if (READING_TYPES.has(state.queue[0]?.step.type)) next()
      else if (ready) check()
    }
    window.addEventListener('keydown', onKey)
    return () => window.removeEventListener('keydown', onKey)
  }, [])

  const stats = {
    accuracy: state.answers ? Math.round((state.rightAnswers / state.answers) * 100) : 100,
    seconds: Math.round(((state.endedAt ?? Date.now()) - state.startedAt) / 1000),
    bestCombo: state.bestCombo,
    mistakes: state.mistakes,
  }

  if (state.phase === 'complete' && result) {
    return (
      <LessonComplete
        mode={lesson.scope === 'section' ? 'section' : state.mode}
        result={result}
        stats={stats}
        learnedTerms={[...metTerms.current].filter((id) => unknownTerms.has(id))}
        guest={authStatus === 'guest'}
        onContinue={() => navigate('/learn')}
        onSave={() => navigate('/signup')}
      />
    )
  }
  if (state.phase === 'failed') {
    return <TrialFailed stats={stats} onRetry={onRestart} onLeave={() => navigate('/learn')} />
  }

  const ui = STEP_UI[card.step.type]
  const revealed = state.phase === 'feedback'
  const docs = card.step.type === 'spot' ? [] : stepDocs(card.step)
  const docLabel = docs.length > 1 ? COMPARE_LABEL : DOC_LABEL
  const { label: stepLabel, Icon: StepIcon } = docs.length && ui.Component !== AllocateStep ? docLabel : ui
  const story = card.step.storyOf && card.step.type !== 'story' ? getLesson(card.step.storyOf)?.story : null
  const newTerms = stepTerms(card.step).filter((id) => unknownTerms.has(id))

  return (
    <TermContext.Provider value={termContext}>
    <div className={`player player--${state.mode}${calcOpen ? ' has-calc' : ''}`}>
      <header className="player__header">
        <button className="player__icon-btn" onClick={quit} aria-label="Quit lesson">
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
            aria-label="Lesson progress"
            aria-valuemin={0}
            aria-valuemax={100}
            aria-valuenow={Math.round(progressOf(state) * 100)}
          >
            <span style={{ width: `${Math.max(progressOf(state) * 100, 3)}%` }} />
          </div>
        </div>

        {state.mode === 'boss' && (
          <div className="player__strikes" aria-label={`${state.mistakes} of ${BOSS_STRIKES} strikes`}>
            {Array.from({ length: BOSS_STRIKES }, (_, i) => (
              <span key={i} className={i < state.mistakes ? 'strike is-hit' : 'strike'}>
                <X />
              </span>
            ))}
          </div>
        )}

        <span
          className={revealed && !state.correct ? 'player__hearts is-hit' : 'player__hearts'}
          aria-label={`${hearts} of ${MAX_HEARTS} hearts`}
        >
          <Heart fill={hearts > 0 ? 'currentColor' : 'none'} />
          <span className="tabular">{hearts}</span>
        </span>

        <button className="player__icon-btn player__calc" onClick={() => setCalcOpen(true)} aria-label="Open calculator">
          <Calculator />
        </button>

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
          <div className="step__head">
            <p className={`step__label step__label--${card.step.type}`}>
              <StepIcon /> {stepLabel}
            </p>
            {hasVoice(card.step.id) && (
              <button className="step__hear" onClick={() => playVoice(card.step.id)} aria-label="Hear the Wolf say it">
                <Volume2 /> Hear it
              </button>
            )}
          </div>
          {newTerms.length > 0 && (
            <div className="newwords">
              <span className="newwords__label">
                New word{newTerms.length > 1 ? 's' : ''}
              </span>
              {newTerms.map((id) => (
                <Term key={id} id={id} chip>
                  {glossary[id].term}
                </Term>
              ))}
              <span className="newwords__hint">Tap a gold word to see what it means.</span>
            </div>
          )}
          {story && <StoryRecall story={story} />}
          {card.step.context && (
            <div className="scenario">
              <WolfMark size="md" />
              <p>
                <Rich text={card.step.context} />
              </p>
            </div>
          )}
          {docs.length > 0 && <Documents docs={docs} />}
          <ui.Component
            card={card}
            answer={state.answer}
            setAnswer={(value) => dispatch({ type: 'answer', value })}
            revealed={revealed}
            correct={state.correct}
            onPair={(ok, n) => (ok ? sfx.pair(n) : sfx.wrong())}
            onSolved={solvedOnItsOwn}
          />
        </div>
      </main>

      <FeedbackBar
        phase={state.phase}
        card={card}
        ready={ready}
        correct={state.correct}
        combo={state.combo}
        mode={state.mode}
        mistakes={state.mistakes}
        strikes={BOSS_STRIKES}
        seed={state.answers}
        answer={state.answer}
        onCheck={check}
        onNext={next}
      />

      {!calcOpen && <CalculatorTab onOpen={() => setCalcOpen(true)} />}
      <CalculatorPanel
        open={calcOpen}
        onClose={() => setCalcOpen(false)}
        canUse={card.step.type === 'number' && state.phase === 'answer'}
        onUse={(value) => {
          dispatch({ type: 'answer', value })
          // On narrow screens the calculator covers the question; get out of the way.
          if (window.matchMedia('(max-width: 1000px)').matches) setCalcOpen(false)
        }}
      />

      {outOfHearts && !quitting && (
        <Dialog
          icon={<HeartCrack className="dialog__heart" />}
          title="Out of hearts."
          actions={
            <>
              <button className="btn btn--danger btn--block" onClick={actions.refillHearts} autoFocus>
                Refill hearts
              </button>
              <button className="btn btn--ghost btn--block" onClick={() => navigate('/learn')}>
                Quit lesson
              </button>
            </>
          }
        >
          Even wolves rest. Refill to finish this lesson, or come back later.
        </Dialog>
      )}

      {quitting && (
        <Dialog
          title="Leaving already?"
          onEscape={() => setQuitting(false)}
          actions={
            <>
              <button className="btn btn--block" onClick={() => setQuitting(false)} autoFocus>
                Keep going
              </button>
              <button className="btn btn--ghost btn--block" onClick={() => navigate('/learn')}>
                Quit
              </button>
            </>
          }
        >
          Quit now and you lose this lesson's progress. Hearts you've lost stay lost.
        </Dialog>
      )}
    </div>
    </TermContext.Provider>
  )
}
