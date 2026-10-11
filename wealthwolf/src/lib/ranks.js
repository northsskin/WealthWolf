// Thresholds are set against the course: Section 1 (Everyday Money) pays about
// 1,200 XP before perfect bonuses, so clearing it lands you at Wolf. Alpha needs
// the sections after it.
export const RANKS = [
  { id: 'pup', name: 'Pup', minXp: 0, tagline: 'Eyes open. Learning the scent.' },
  { id: 'scout', name: 'Scout', minXp: 150, tagline: "You know the terrain. Now move." },
  { id: 'hunter', name: 'Hunter', minXp: 500, tagline: 'Tracking every dollar.' },
  { id: 'wolf', name: 'Wolf', minXp: 1000, tagline: 'Disciplined. Dangerous. Diversified.' },
  { id: 'alpha', name: 'Alpha', minXp: 2000, tagline: 'The pack follows your lead.' },
]

export function rankForXp(xp) {
  let index = 0
  for (let i = 0; i < RANKS.length; i++) if (xp >= RANKS[i].minXp) index = i
  const rank = RANKS[index]
  const next = RANKS[index + 1] ?? null
  const progress = next ? (xp - rank.minXp) / (next.minXp - rank.minXp) : 1
  return { rank, next, index, progress, xpToNext: next ? next.minXp - xp : 0 }
}
