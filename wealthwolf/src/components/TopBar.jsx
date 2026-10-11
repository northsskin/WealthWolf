import { useCallback, useRef, useState } from 'react'
import { NavLink } from 'react-router'
import { BookA, Heart } from 'lucide-react'
import Bar from './Bar.jsx'
import RankProgress from './RankProgress.jsx'
import Tally from './Tally.jsx'
import AccountMenu from './AccountMenu.jsx'
import { liveStreak, MAX_HEARTS, useStore } from '../store/store.js'
import { rankForXp } from '../lib/ranks.js'
import { useDismiss } from '../lib/useDismiss.js'
import './TopBar.css'

export default function TopBar() {
  const xp = useStore((s) => s.xp)
  const hearts = useStore((s) => s.hearts)
  const streak = useStore((s) => liveStreak(s.streak))
  const { rank } = rankForXp(xp)

  const [rankOpen, setRankOpen] = useState(false)
  const rankRef = useRef(null)
  const closeRank = useCallback(() => setRankOpen(false), [])
  useDismiss(rankRef, rankOpen, closeRank)

  return (
    <Bar sticky>
      <NavLink to="/glossary" className="navlink" aria-label="Glossary" title="Glossary: every word you've learned">
        <BookA />
        <span className="navlink__label">Glossary</span>
      </NavLink>
      <nav className="stats" aria-label="Your stats">
        <div className="stats__rank" ref={rankRef}>
          <button
            className="stat stat--rank"
            aria-expanded={rankOpen}
            aria-label={`Rank: ${rank.name}`}
            onClick={() => setRankOpen((open) => !open)}
          >
            <span className="stat__badge" aria-hidden="true">
              {rank.name[0]}
            </span>
            <span className="stat__rank-name">{rank.name}</span>
          </button>
          {rankOpen && (
            <div className="stats__popover" role="dialog" aria-label="Rank progress">
              <RankProgress xp={xp} />
            </div>
          )}
        </div>

        <span
          className={streak > 0 ? 'stat stat--streak' : 'stat stat--streak is-cold'}
          title={streak > 0 ? `${streak} day streak` : 'No streak yet. Finish a lesson to start one.'}
          aria-label={`${streak} day streak`}
        >
          <Tally />
          <span className="figure">{streak}</span>
        </span>

        <span className="stat stat--xp" title="Total XP" aria-label={`${xp} XP`}>
          <span className="stat__unit">XP</span>
          <span className="figure">{xp}</span>
        </span>

        <span
          className={hearts > 0 ? 'stat stat--hearts' : 'stat stat--hearts is-empty'}
          title={`${hearts} of ${MAX_HEARTS} hearts`}
          aria-label={`${hearts} of ${MAX_HEARTS} hearts`}
        >
          <Heart fill={hearts > 0 ? 'currentColor' : 'none'} />
          <span className="figure">{hearts}</span>
        </span>
      </nav>
      <AccountMenu />
    </Bar>
  )
}
