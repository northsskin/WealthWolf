import { useState } from 'react'
import { Link } from 'react-router'
import { ArrowLeft, Lock, Search, X } from 'lucide-react'
import TopBar from '../components/TopBar.jsx'
import PenMark from '../components/PenMark.jsx'
import { ReceiptLine } from '../components/lesson/LessonComplete.jsx'
import { currentLessonId, getLesson, glossary, lessons, modules, termOrigins } from '../lib/content.js'
import { dayKey, daysBetween } from '../lib/dates.js'
import {
  DRILL_SIZE,
  MIN_DRILL_WORDS,
  STATUS_LABEL,
  learnedWords,
  wordModule,
  wordStatus,
  wordsInPathOrder,
} from '../lib/words.js'
import { useStore } from '../store/store.js'
import '../components/SkillPath.css'
import './Learn.css'
import './Glossary.css'

const STATUS_ORDER = ['solid', 'practising', 'shaky', 'new']
const plural = (n, word) => `${n} ${word}${n === 1 ? '' : 's'}`

function learnedOn(key) {
  const days = daysBetween(key, dayKey())
  if (days === 0) return 'today'
  if (days === 1) return 'yesterday'
  const [y, m, d] = key.split('-').map(Number)
  return new Date(y, m - 1, d).toLocaleDateString('en-US', { month: 'short', day: 'numeric' })
}

// Headwords file under their first letter; "50/30/20 rule" and "401(k)" go under #.
const letterOf = (id) => {
  const first = glossary[id].term[0].toUpperCase()
  return /[A-Z]/.test(first) ? first : '#'
}

const byTerm = (a, b) => glossary[a].term.localeCompare(glossary[b].term, 'en', { numeric: true })

export default function Glossary() {
  const terms = useStore((s) => s.terms)
  const wordStats = useStore((s) => s.wordStats)
  const completed = useStore((s) => s.completed)
  const [query, setQuery] = useState('')
  const [order, setOrder] = useState('unit')

  const learned = learnedWords(terms)
  const total = wordsInPathOrder.length
  const statusOf = (id) => wordStatus(wordStats[id])
  const counts = Object.fromEntries(STATUS_ORDER.map((s) => [s, learned.filter((id) => statusOf(id) === s).length]))

  // Search reads what you can see: a learned word's meaning and example, a locked word's name only.
  const q = query.trim().toLowerCase()
  const matches = (id) => {
    if (!q) return true
    const { term, definition, example } = glossary[id]
    const fields = terms[id] ? [term, definition, example] : [term]
    return fields.some((text) => text?.toLowerCase().includes(q))
  }
  const shown = wordsInPathOrder.filter(matches)
  const nothingFound = q && shown.length === 0

  const entry = (id) => <Word key={id} id={id} status={statusOf(id)} metOn={terms[id]} />

  return (
    <div className="gloss">
      <TopBar />
      <main className="gloss__body">
        <header className="gloss__head">
          <Link to="/learn" className="backlink">
            <ArrowLeft /> Back to the path
          </Link>
          <h1 className="display gloss__title">Glossary</h1>
          <p className="gloss__sub">
            Every word the course teaches. The ones you’ve met in a lesson are written out here with an example.
            The rest show which unit teaches them.
          </p>
        </header>

        <Aside learned={learned} total={total} counts={counts} completed={completed} />

        <div className="gloss__list">
          <div className="gloss__tools">
            <label className="gsearch">
              <Search aria-hidden="true" />
              <input
                type="search"
                value={query}
                onChange={(event) => setQuery(event.target.value)}
                placeholder="Find a word"
                aria-label="Find a word"
              />
              {query && (
                <button type="button" className="gsearch__clear" onClick={() => setQuery('')} aria-label="Clear search">
                  <X />
                </button>
              )}
            </label>
            <div className="seg" role="group" aria-label="Order words">
              <button type="button" aria-pressed={order === 'unit'} onClick={() => setOrder('unit')}>
                By unit
              </button>
              <button type="button" aria-pressed={order === 'az'} onClick={() => setOrder('az')}>
                A–Z
              </button>
            </div>
          </div>

          {nothingFound && (
            <p className="gloss__empty">
              No word matches “{query.trim()}”.{' '}
              <button type="button" className="textbtn" onClick={() => setQuery('')}>
                Clear the search
              </button>
            </p>
          )}

          {order === 'unit' &&
            modules.map((mod, i) => {
              const ids = shown.filter((id) => wordModule(id) === mod.id)
              if (!ids.length) return null
              const all = wordsInPathOrder.filter((id) => wordModule(id) === mod.id)
              const known = ids.filter((id) => terms[id])
              const ahead = ids.filter((id) => !terms[id])
              const knownInUnit = all.filter((id) => terms[id]).length
              return (
                <section
                  key={mod.id}
                  className={`unit gunit${knownInUnit === all.length ? ' unit--completed' : knownInUnit ? '' : ' unit--locked'}`}
                  aria-labelledby={`gunit-${mod.id}`}
                >
                  <header className="unit__header">
                    <span className="figure unit__no">{String(i + 1).padStart(2, '0')}</span>
                    <h2 id={`gunit-${mod.id}`} className="display unit__title">
                      {mod.title}
                    </h2>
                    <span className="figure unit__count" aria-label={`${knownInUnit} of ${all.length} words learned`}>
                      {knownInUnit}/{all.length}
                    </span>
                  </header>
                  {known.length > 0 && <dl className="words">{known.map(entry)}</dl>}
                  {ahead.length > 0 && <Ahead ids={ahead} afterSome={known.length > 0} />}
                </section>
              )
            })}

          {order === 'az' && (
            <>
              {[...new Set(learned.filter(matches).sort(byTerm).map(letterOf))].map((letter) => (
                <section key={letter} className="gletter" aria-label={`Words under ${letter}`}>
                  <h2 className="display gletter__head">{letter}</h2>
                  <dl className="words">
                    {learned
                      .filter((id) => matches(id) && letterOf(id) === letter)
                      .sort(byTerm)
                      .map(entry)}
                  </dl>
                </section>
              ))}
              {!q && learned.length === 0 && (
                <p className="gloss__empty">No words yet. Every word you meet in a lesson is filed here.</p>
              )}
              {!q && learned.length < total && (
                <p className="gloss__footnote">
                  {plural(total - learned.length, 'more word')} still ahead. <strong>By unit</strong> shows where each
                  one is taught.
                </p>
              )}
              {q && !nothingFound && learned.filter(matches).length === 0 && (
                <p className="gloss__empty">
                  Only words you haven’t met yet match. <strong>By unit</strong> shows where they’re taught.
                </p>
              )}
            </>
          )}
        </div>
      </main>
    </div>
  )
}

function Word({ id, status, metOn }) {
  const { term, definition, example } = glossary[id]
  const lesson = getLesson(termOrigins[id]?.lessonId)
  return (
    <div className={`word word--${status}`}>
      <dt className="word__head">
        <span className="word__term">
          {term}
          {status === 'shaky' && <PenMark kind="underline" className="word__mark" />}
        </span>
        {status !== 'new' && <span className={`wtag wtag--${status}`}>{STATUS_LABEL[status]}</span>}
      </dt>
      <dd className="word__def">{definition}</dd>
      {example && (
        <dd className="word__example">
          <span className="eyebrow">Example</span> {example}
        </dd>
      )}
      <dd className="word__meta">
        Met in {lesson ? `“${lesson.title}”` : 'a lesson'} · {learnedOn(metOn)}
      </dd>
    </div>
  )
}

// Words not met yet: names only, in pencil, with the lesson that teaches each one.
function Ahead({ ids, afterSome }) {
  return (
    <div className="ahead">
      <p className="eyebrow">
        {afterSome ? 'Still ahead in this unit' : 'Taught in this unit'} · {ids.length}
      </p>
      <ul className="ahead__list">
        {ids.map((id) => {
          const lesson = getLesson(termOrigins[id]?.lessonId)
          return (
            <li key={id} className="ahead__word" title={lesson ? `Taught in “${lesson.title}”` : undefined}>
              <Lock aria-hidden="true" />
              {glossary[id].term}
            </li>
          )
        })}
      </ul>
    </div>
  )
}

function Aside({ learned, total, counts, completed }) {
  const n = learned.length
  const canDrill = n >= MIN_DRILL_WORDS
  const nextLesson = currentLessonId(completed)

  let copy
  if (canDrill) {
    copy = `${Math.min(DRILL_SIZE, n)} quick questions on words you’ve learned: read a meaning and pick the word, or the other way round. ${
      counts.shaky ? 'Shaky words come up first.' : 'Missed words come back until you get them.'
    }`
  } else if (n === 0) {
    copy = `Words you meet in lessons collect here. The drill opens once you’ve learned ${MIN_DRILL_WORDS}.`
  } else {
    copy = `The drill opens once you’ve learned ${MIN_DRILL_WORDS} words. You’ve learned ${n}, so ${MIN_DRILL_WORDS - n} to go.`
  }

  return (
    <aside className="gloss__aside" aria-label="Your words">
      <section className="panel">
        <p className="eyebrow">Words learned</p>
        <p className="panel__big">
          <span className="figure">{n}</span> of {total}
        </p>
        <div
          className="gbar"
          role="progressbar"
          aria-label="Words learned"
          aria-valuemin={0}
          aria-valuemax={total}
          aria-valuenow={n}
        >
          <span style={{ width: `${(n / total) * 100}%` }} />
        </div>
        {n > 0 && (
          <dl className="receipt__lines gloss__tally">
            {STATUS_ORDER.map((s) => (
              <ReceiptLine key={s} label={STATUS_LABEL[s]} value={counts[s]} />
            ))}
          </dl>
        )}
      </section>

      <section className="panel">
        <p className="eyebrow">Review</p>
        <h2 className="display gpanel__title">Word drill</h2>
        <p className="panel__copy">{copy}</p>
        {canDrill ? (
          <Link to="/glossary/drill" className="btn btn--block gpanel__btn">
            Start drill
          </Link>
        ) : n === 0 && nextLesson === lessons[0].id ? (
          <Link to={`/lesson/${nextLesson}`} className="btn btn--block gpanel__btn">
            Start lesson one
          </Link>
        ) : (
          <button className="btn btn--block gpanel__btn" disabled>
            Start drill
          </button>
        )}
      </section>
    </aside>
  )
}
