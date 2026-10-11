import { useState } from 'react'
import { Link, Navigate, useNavigate, useParams } from 'react-router'
import { ChartLine, HeartCrack, X } from 'lucide-react'
import LessonPlayer from '../components/lesson/LessonPlayer.jsx'
import WolfMark from '../components/WolfMark.jsx'
import { canPlay, getLesson, lessonStatus } from '../lib/content.js'
import { useAuth } from '../lib/auth.js'
import { actions, getState, useStore } from '../store/store.js'
import '../components/lesson/shared.css'
import './Lesson.css'

export default function Lesson() {
  const { lessonId } = useParams()
  const navigate = useNavigate()
  const completed = useStore((s) => s.completed)
  const { status: authStatus } = useAuth()
  const [attempt, setAttempt] = useState(0)
  const [playing, setPlaying] = useState(() => getState().hearts > 0)

  const lesson = getLesson(lessonId)
  if (!lesson) {
    return (
      <Gate
        icon={<WolfMark size="lg" />}
        title="Lost the scent."
        body="That lesson doesn't exist."
        actions={
          <Link className="btn fb__btn" to="/learn">
            Back to path
          </Link>
        }
      />
    )
  }
  if (lessonStatus(lesson.id, completed) === 'locked') return <Navigate to="/learn" replace />
  // Lesson one is free; past it, you need an account (wait until we know whether you have one).
  if (authStatus === 'loading') return null
  if (!canPlay(lesson, authStatus === 'user')) {
    return <Navigate to={`/signup?next=${encodeURIComponent(`/lesson/${lesson.id}`)}`} replace />
  }

  if (lesson.type === 'sim') {
    return (
      <Gate
        icon={<ChartLine className="gate__icon--gold" />}
        eyebrow="Coming soon"
        title="Portfolio Simulator"
        body="Build a portfolio with fake money and fast-forward 30 years. It's still being built, so you can skip ahead for now. No XP for skipping."
        actions={
          <>
            <Link className="btn btn--ghost fb__btn" to="/learn">
              Back to path
            </Link>
            <button
              className="btn fb__btn"
              onClick={() => {
                actions.completeLesson(lesson, { skipped: true })
                navigate('/learn')
              }}
            >
              Skip for now
            </button>
          </>
        }
      />
    )
  }

  if (!playing) {
    return (
      <Gate
        icon={<HeartCrack className="gate__icon--red" />}
        title="Out of hearts."
        body="Even wolves rest. Refill to keep hunting."
        actions={
          <>
            <Link className="btn btn--ghost fb__btn" to="/learn">
              Back to path
            </Link>
            <button
              className="btn btn--danger fb__btn"
              onClick={() => {
                actions.refillHearts()
                setPlaying(true)
              }}
              autoFocus
            >
              Refill hearts
            </button>
          </>
        }
      />
    )
  }

  return (
    <LessonPlayer
      key={`${lesson.id}:${attempt}`}
      lesson={lesson}
      onRestart={() => {
        setAttempt((n) => n + 1)
        setPlaying(getState().hearts > 0)
      }}
    />
  )
}

function Gate({ icon, eyebrow, title, body, actions }) {
  return (
    <div className="gate">
      <header className="gate__header">
        <Link to="/learn" className="gate__close" aria-label="Back to path">
          <X />
        </Link>
      </header>
      <main className="gate__main">
        {icon}
        {eyebrow && <p className="eyebrow gate__eyebrow">{eyebrow}</p>}
        <h1 className="display gate__title">{title}</h1>
        <p className="gate__body">{body}</p>
      </main>
      <footer className="fb">
        <div className="fb__inner">{actions}</div>
      </footer>
    </div>
  )
}
