import { useState } from 'react'
import { Link } from 'react-router'
import { Heart, RotateCcw } from 'lucide-react'
import Tally from '../components/Tally.jsx'
import TopBar from '../components/TopBar.jsx'
import SkillPath from '../components/SkillPath.jsx'
import SectionHeader from '../components/SectionHeader.jsx'
import { currentLessonId, getLesson, sections } from '../lib/content.js'
import RankProgress from '../components/RankProgress.jsx'
import { actions, liveStreak, MAX_HEARTS, useStore } from '../store/store.js'
import { dayKey } from '../lib/dates.js'
import { MIN_DRILL_WORDS, wordStatus } from '../lib/words.js'
import { useAuth } from '../lib/auth.js'
import WolfMark from '../components/WolfMark.jsx'
import './Learn.css'

export default function Learn() {
  const xp = useStore((s) => s.xp)
  const hearts = useStore((s) => s.hearts)
  const streak = useStore((s) => liveStreak(s.streak))
  const safeToday = useStore((s) => s.streak.lastActiveDay === dayKey())
  const words = useStore((s) => Object.keys(s.terms).length)
  const shaky = useStore((s) => Object.values(s.wordStats).filter((stat) => wordStatus(stat) === 'shaky').length)
  const lessonsDone = useStore((s) => Object.keys(s.completed).length)
  const { status: authStatus } = useAuth()
  const completed = useStore((s) => s.completed)
  // Open on the section the player is working through; the picker can show any other.
  const currentSectionId = getLesson(currentLessonId(completed))?.sectionId ?? sections[sections.length - 1].id
  const [sectionId, setSectionId] = useState(currentSectionId)
  const section = sections.find((s) => s.id === sectionId) ?? sections[0]

  function pickSection(id) {
    setSectionId(id)
    window.scrollTo({ top: 0 })
  }
  const unsaved = authStatus === 'guest' && lessonsDone > 0

  function reset() {
    if (window.confirm('Wipe all XP, streak and lesson progress? This cannot be undone.')) {
      actions.resetProgress()
    }
  }

  let streakCopy
  if (safeToday) streakCopy = "Streak's safe for today. Come back tomorrow."
  else if (streak > 0) streakCopy = `Finish a lesson today or lose your ${streak}-day streak.`
  else streakCopy = 'No streak yet. One lesson lights it.'

  let wordsCopy
  if (shaky > 0) wordsCopy = `${shaky} shaky. Drill ${shaky === 1 ? 'it' : 'them'} before ${shaky === 1 ? 'it slips' : 'they slip'}.`
  else if (words >= MIN_DRILL_WORDS) wordsCopy = 'Every word you’ve learned, with what it means. Drill them any time.'
  else wordsCopy = 'Words from your lessons collect here, with what they mean.'

  return (
    <div className="learn">
      <TopBar />
      <div className="learn__body">
        <main className="learn__main">
          {unsaved && (
            <aside className="savenote" aria-label="Save your progress">
              <WolfMark size="sm" />
              <p>
                <strong>
                  {lessonsDone === 1 ? 'Lesson one is done, but it' : 'Your progress'} only lives in this browser.
                </strong>{' '}
                Create a free account to save it and unlock the rest of the path.
              </p>
              <Link to="/signup" className="btn savenote__btn">
                Create account
              </Link>
            </aside>
          )}
          <SectionHeader
            section={section}
            completed={completed}
            currentSectionId={currentSectionId}
            onPick={pickSection}
          />
          <SkillPath key={section.id} section={section} onPickSection={pickSection} />
        </main>

        <aside className="learn__aside" aria-label="Progress">
          <section className="panel">
            <RankProgress xp={xp} />
          </section>

          <section className={streak > 0 ? 'panel panel--streak is-lit' : 'panel panel--streak'}>
            <Tally />
            <div>
              <p className="panel__big">
                <span className="figure">{streak}</span> day{streak === 1 ? '' : 's'}
              </p>
              <p className="panel__copy">{streakCopy}</p>
            </div>
          </section>

          <section className="panel">
            <p className="eyebrow">Glossary</p>
            <p className="panel__big">
              <span className="figure">{words}</span> word{words === 1 ? '' : 's'} learned
            </p>
            <p className="panel__copy">{wordsCopy}</p>
            <Link to={shaky > 0 ? '/glossary/drill' : '/glossary'} className="btn btn--ghost btn--block panel__link">
              {shaky > 0 ? 'Drill shaky words' : 'Open glossary'}
            </Link>
          </section>

          <section className="panel panel--dev">
            <p className="eyebrow">Prototype controls</p>
            <div className="panel__actions">
              <button
                className="btn btn--ghost"
                onClick={actions.refillHearts}
                disabled={hearts === MAX_HEARTS}
              >
                <Heart /> Refill
              </button>
              <button className="btn btn--ghost" onClick={reset}>
                <RotateCcw /> Reset
              </button>
            </div>
          </section>
        </aside>
      </div>
    </div>
  )
}
