import { RANKS, rankForXp } from '../lib/ranks.js'
import './RankProgress.css'

export default function RankProgress({ xp }) {
  const { rank, next, index, progress, xpToNext } = rankForXp(xp)

  return (
    <div className="rankprog">
      <p className="eyebrow">Current rank</p>
      <p className="display rankprog__name">{rank.name}</p>
      <p className="rankprog__tagline">{rank.tagline}</p>

      <div
        className="rankprog__bar"
        role="progressbar"
        aria-valuemin={0}
        aria-valuemax={100}
        aria-valuenow={Math.round(progress * 100)}
        aria-label={next ? `Progress to ${next.name}` : 'Top rank reached'}
      >
        <span style={{ width: `${progress * 100}%` }} />
      </div>
      <p className="rankprog__next">
        {next ? (
          <>
            <span className="figure">{xpToNext} XP</span> to {next.name}
          </>
        ) : (
          'Top of the pack.'
        )}
      </p>

      <ol className="rankprog__ladder" aria-label="All ranks">
        {RANKS.map((r, i) => (
          <li key={r.id} className={i <= index ? 'is-earned' : undefined} title={`${r.name}: ${r.minXp} XP`}>
            {r.name}
          </li>
        ))}
      </ol>
    </div>
  )
}
