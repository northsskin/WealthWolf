import './PenMark.css'

// The Wolf's red pen. Each mark is a hand-drawn path that draws itself on,
// so the page looks like it's being marked up as you read it.
const PATHS = {
  // A loose oval that overshoots where it started, like a real pen circle.
  circle: { viewBox: '0 0 120 60', d: 'M86 6 C 50 0, 8 8, 6 30 C 4 52, 60 58, 98 50 C 122 44, 120 14, 82 8 C 70 6, 58 8, 48 11' },
  // A loose loop for wide rows: steep sides, so it rings the text without crossing it.
  ring: { viewBox: '0 0 200 40', d: 'M40 4 C 110 0, 186 1, 195 14 C 202 30, 150 38, 80 37 C 30 36, 3 32, 4 18 C 5 7, 36 3, 100 3' },
  strike: { viewBox: '0 0 200 20', d: 'M2 12 C 40 8, 90 13, 140 9 S 190 10, 198 8' },
  underline: { viewBox: '0 0 200 20', d: 'M2 8 C 60 12, 130 6, 198 10 M 12 16 C 70 19, 140 13, 190 17' },
  check: { viewBox: '0 0 40 40', d: 'M6 22 L 16 32 L 35 7' },
  cross: { viewBox: '0 0 40 40', d: 'M8 8 L 32 32 M 32 8 L 8 32' },
  arrow: { viewBox: '0 0 60 24', d: 'M2 14 C 18 8, 34 18, 52 12 M 42 4 L 54 12 L 44 21' },
}

export default function PenMark({ kind, delay = 0, className = '', tone = 'red' }) {
  const { viewBox, d } = PATHS[kind]
  return (
    <svg
      className={`penmark penmark--${kind} penmark--${tone} ${className}`}
      viewBox={viewBox}
      preserveAspectRatio="none"
      aria-hidden="true"
      style={{ '--pen-delay': `${delay}ms` }}
    >
      <path d={d} pathLength="1" />
    </svg>
  )
}
