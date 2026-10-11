import { useCallback, useEffect, useRef, useState } from 'react'
import { useNavigate } from 'react-router'
import { BookOpen, ChartLine, Check, Lock, MessageSquareText, ReceiptText, RefreshCw, Scale, ScanSearch, Shapes } from 'lucide-react'
import WolfMark from './WolfMark.jsx'
import { canPlay, getLesson, lessonStatus, currentLessonId, sections } from '../lib/content.js'
import { useAuth } from '../lib/auth.js'
import { useDismiss } from '../lib/useDismiss.js'
import { useStore, xpReward } from '../store/store.js'
import './SkillPath.css'

// Path geometry, in px inside a fixed-width track so the SVG trail and the
// node buttons share one coordinate system.
const TRACK_W = 320
const ROW_H = 124
const PAD_Y = 36
const SWING = [0, 50, 82, 50, 0, -50, -82, -50]
const POPOVER_W = 300 // matches --float-w

// Lessons are told apart by format, so the path shows what kind of stop is next.
const FORMATS = {
  concept: { label: 'Lesson', Icon: BookOpen },
  document: { label: 'Read the document', Icon: ReceiptText },
  story: { label: 'Money story', Icon: MessageSquareText },
  spot: { label: 'Spot the problem', Icon: ScanSearch },
  sort: { label: 'Sort it', Icon: Shapes },
  call: { label: 'Make the call', Icon: Scale },
}
const TYPES = {
  review: { label: 'Smart Review', Icon: RefreshCw },
  sim: { label: 'Simulator', Icon: ChartLine },
  boss: { label: 'Den Trial', Icon: null },
}
const SECTION_TRIAL = { label: 'Section Trial', Icon: null }
const kindOf = (lesson) => {
  if (lesson.type === 'lesson') return FORMATS[lesson.format] ?? FORMATS.concept
  return lesson.scope === 'section' ? SECTION_TRIAL : TYPES[lesson.type]
}

function nodePoints(count, flip) {
  return Array.from({ length: count }, (_, i) => ({
    x: TRACK_W / 2 + SWING[i % SWING.length] * (flip ? -1 : 1),
    y: PAD_Y + ROW_H / 2 + i * ROW_H,
  }))
}

function curve(a, b) {
  const dy = (b.y - a.y) / 2
  return `M ${a.x} ${a.y} C ${a.x} ${a.y + dy}, ${b.x} ${b.y - dy}, ${b.x} ${b.y}`
}

// One section of the path: its units in order, then its Section Trial.
export default function SkillPath({ section, onPickSection }) {
  const completed = useStore((s) => s.completed)
  const currentId = currentLessonId(completed)
  const [openId, setOpenId] = useState(null)
  const currentRef = useRef(null)

  // Land the player on their next lesson, not the top of the path.
  useEffect(() => {
    currentRef.current?.scrollIntoView({ block: 'center' })
  }, [])

  const trial = section.trial ? getLesson(section.trial.id) : null
  const next = sections[sections.indexOf(section) + 1]
  const cleared = section.units.every((mod) => mod.lessons.every((l) => completed[l.id])) && (!trial || completed[trial.id])
  const shared = { completed, currentId, openId, setOpenId, currentRef }

  return (
    <div className="path">
      {section.units.map((mod, i) => (
        <ModuleSection key={mod.id} mod={mod} number={i + 1} {...shared} />
      ))}
      {trial && (
        <ModuleSection
          mod={{
            id: trial.id,
            title: trial.title,
            description: trial.summary,
            wolfLine: 'Every unit in this section, in one sitting. Pass it and the next section opens.',
            lessons: [trial],
          }}
          number={section.units.length + 1}
          label="End"
          {...shared}
        />
      )}
      <div className="path__end">
        <WolfMark size="lg" />
        <p className="display path__end-title">{cleared ? 'Section cleared. Respect.' : 'More hunts ahead.'}</p>
        {next ? (
          <>
            <p className="path__end-sub">
              Next: Section {next.number} · {next.title}
            </p>
            <button className="btn btn--ghost path__next" onClick={() => onPickSection(next.id)}>
              Go to Section {next.number}
            </button>
          </>
        ) : (
          <p className="path__end-sub">More sections are being written. Stay hungry.</p>
        )}
      </div>
    </div>
  )
}

function ModuleSection({ mod, number, label, completed, currentId, openId, setOpenId, currentRef }) {
  const points = nodePoints(mod.lessons.length, number % 2 === 0)
  const done = mod.lessons.filter((l) => completed[l.id]).length
  const total = mod.lessons.length
  const state =
    done === total ? 'completed' : mod.lessons.some((l) => l.id === currentId) ? 'active' : 'locked'

  return (
    <section className={`unit unit--${state}`} aria-labelledby={`unit-${mod.id}`}>
      <header className="unit__header">
        <span className="figure unit__no">{label ?? String(number).padStart(2, '0')}</span>
        <div className="unit__heading">
          <h2 id={`unit-${mod.id}`} className="display unit__title">
            {mod.title}
          </h2>
          <p className="unit__desc">{mod.description}</p>
        </div>
        <span className="figure unit__count" aria-label={`${done} of ${total} complete`}>
          {state === 'completed' ? 'Cleared' : `${done}/${total}`}
        </span>
      </header>

      <p className="unit__wolf">
        <WolfMark size="xs" />
        <span>{mod.wolfLine}</span>
      </p>

      <div className="unit__track" style={{ width: TRACK_W, height: PAD_Y * 2 + ROW_H * total }}>
        <svg className="unit__trail" width={TRACK_W} height={PAD_Y * 2 + ROW_H * total} aria-hidden="true">
          {points.slice(1).map((point, i) => (
            <path
              key={mod.lessons[i].id}
              d={curve(points[i], point)}
              className={completed[mod.lessons[i].id] ? 'trail is-done' : 'trail'}
            />
          ))}
        </svg>

        {mod.lessons.map((lesson, i) => (
          <PathNode
            key={lesson.id}
            lesson={lesson}
            point={points[i]}
            status={lessonStatus(lesson.id, completed)}
            isCurrent={lesson.id === currentId}
            open={openId === lesson.id}
            setOpenId={setOpenId}
            currentRef={currentRef}
          />
        ))}
      </div>
    </section>
  )
}

function PathNode({ lesson, point, status, isCurrent, open, setOpenId, currentRef }) {
  const wrapRef = useRef(null)
  const close = useCallback(() => setOpenId(null), [setOpenId])
  useDismiss(wrapRef, open, close)

  const isBoss = lesson.type === 'boss'
  let icon
  if (isBoss) icon = <WolfMark mono size="md" />
  else if (status === 'completed') icon = <Check />
  else {
    // Locked stops still show what kind of lesson they are, pencilled in.
    const { Icon } = kindOf(lesson)
    icon = <Icon />
  }

  // Keep the popover inside the track while its arrow still points at the node.
  const half = POPOVER_W / 2
  const shift = Math.min(Math.max(point.x, half), TRACK_W - half) - point.x

  const setRefs = (el) => {
    wrapRef.current = el
    if (isCurrent) currentRef.current = el
  }

  return (
    <div
      ref={setRefs}
      className={open ? 'node-wrap is-open' : 'node-wrap'}
      style={{ left: point.x, top: point.y }}
    >
      {isCurrent && !open && <span className="node__start">Start</span>}
      <button
        className={`node node--${status} ${isBoss ? 'node--boss' : ''}`}
        style={{ '--tilt': `${((lesson.indexInModule * 7) % 13) - 6}deg` }}
        aria-label={`${lesson.title} (${kindOf(lesson).label}, ${status})`}
        aria-expanded={open}
        onClick={() => setOpenId(open ? null : lesson.id)}
      >
        {icon}
      </button>
      {open && <NodePopover lesson={lesson} status={status} shift={shift} />}
    </div>
  )
}

function NodePopover({ lesson, status, shift }) {
  const navigate = useNavigate()
  const { status: authStatus } = useAuth()
  const start = () => navigate(`/lesson/${lesson.id}`)
  // Past lesson one, a guest is asked for an account instead.
  const needsAccount = status !== 'locked' && authStatus === 'guest' && !canPlay(lesson, false)

  return (
    <div
      className={`popover popover--${status}`}
      role="dialog"
      aria-label={lesson.title}
      style={{ width: POPOVER_W, '--shift': `${shift}px` }}
    >
      <p className="eyebrow popover__type">{kindOf(lesson).label}</p>
      <h3 className="popover__title">{lesson.title}</h3>
      <p className="popover__summary">{lesson.summary}</p>

      {needsAccount && (
        <>
          <p className="popover__locked">
            <Lock /> Lesson one is free. To keep going, make a free account.
          </p>
          <button
            className="btn btn--block popover__cta"
            onClick={() => navigate(`/signup?next=${encodeURIComponent(`/lesson/${lesson.id}`)}`)}
            autoFocus
          >
            Create account to continue
          </button>
        </>
      )}
      {status === 'available' && !needsAccount && (
        <button className="btn btn--block popover__cta" onClick={start} autoFocus>
          Start · +{lesson.xp} XP
        </button>
      )}
      {status === 'completed' && !needsAccount && (
        <button className="btn btn--ghost btn--block popover__cta" onClick={start} autoFocus>
          Practice · +{xpReward(lesson, true)} XP
        </button>
      )}
      {status === 'locked' && (
        <p className="popover__locked">
          <Lock /> Finish everything above to unlock. No shortcuts.
        </p>
      )}
    </div>
  )
}
