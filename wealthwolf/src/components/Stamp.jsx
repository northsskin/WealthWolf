import { useId } from 'react'
import WolfMark from './WolfMark.jsx'
import './Stamp.css'

// A rubber stamp: ring lettering around the Wolf, inked with a little
// texture so it reads as pressed onto the page rather than drawn on it.
export default function Stamp({ text, tone = 'red', className = '', delay = 0, tilt = -10 }) {
  const id = useId().replace(/:/g, '')
  return (
    <span
      className={`stamp stamp--${tone} ${className}`}
      style={{ '--stamp-delay': `${delay}ms`, '--stamp-tilt': `${tilt}deg` }}
      aria-hidden="true"
    >
      <svg viewBox="0 0 200 200" className="stamp__svg">
        <defs>
          <path id={`${id}-ring`} d="M100,100 m-72,0 a72,72 0 1,1 144,0 a72,72 0 1,1 -144,0" />
          <filter id={`${id}-ink`} x="-5%" y="-5%" width="110%" height="110%">
            <feTurbulence type="fractalNoise" baseFrequency="0.9" numOctaves="2" seed="4" result="noise" />
            <feColorMatrix in="noise" type="matrix" values="0 0 0 0 0  0 0 0 0 0  0 0 0 0 0  0 0 0 -2.2 1.6" result="speckle" />
            <feComposite in="SourceGraphic" in2="speckle" operator="in" />
          </filter>
        </defs>
        <g filter={`url(#${id}-ink)`}>
          <circle cx="100" cy="100" r="94" className="stamp__ring" strokeWidth="6" />
          <circle cx="100" cy="100" r="56" className="stamp__ring" strokeWidth="3" />
          <text className="stamp__text">
            <textPath href={`#${id}-ring`} startOffset="0" textLength="440">
              {text}
            </textPath>
          </text>
        </g>
      </svg>
      <WolfMark mono size="lg" className="stamp__wolf" />
    </span>
  )
}
