// Streak icon: a bundle of tally marks, the way you'd count days on a wall.
export default function Tally({ className = '' }) {
  return (
    <svg className={`lucide tally ${className}`} viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeLinecap="round" aria-hidden="true">
      <path d="M5 4v16M9.5 4v16M14 4v16M18.5 4v16M2.5 17 21.5 7" />
    </svg>
  )
}
