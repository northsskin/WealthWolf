import { createContext, useContext, useEffect, useId, useLayoutEffect, useRef, useState } from 'react'
import { glossary } from '../lib/content.js'
import './Term.css'

// The lesson player tells terms which ones the learner hasn't met yet.
export const TermContext = createContext({ isNew: () => false })

// A glossary word: tap it to see what it means.
export default function Term({ id, children, chip = false }) {
  const entry = glossary[id]
  const fresh = useContext(TermContext).isNew(id)
  const [open, setOpen] = useState(false)
  const wrap = useRef(null)
  const pop = useRef(null)
  const popId = useId()

  useEffect(() => {
    if (!open) return
    const onPointer = (event) => {
      if (!wrap.current?.contains(event.target)) setOpen(false)
    }
    const onKey = (event) => {
      if (event.key !== 'Escape') return
      event.stopPropagation() // close the definition, not the lesson
      setOpen(false)
    }
    document.addEventListener('pointerdown', onPointer)
    document.addEventListener('keydown', onKey)
    return () => {
      document.removeEventListener('pointerdown', onPointer)
      document.removeEventListener('keydown', onKey)
    }
  }, [open])

  // Keep the card on screen: nudge it sideways, and flip above the word near the bottom.
  useLayoutEffect(() => {
    const el = pop.current
    if (!open || !el) return
    el.style.setProperty('--dx', '0px')
    el.dataset.side = 'below'
    const margin = 12
    const rect = el.getBoundingClientRect()
    let dx = 0
    if (rect.left < margin) dx = margin - rect.left
    else if (rect.right > window.innerWidth - margin) dx = window.innerWidth - margin - rect.right
    el.style.setProperty('--dx', `${dx}px`)
    if (rect.bottom > window.innerHeight - margin) el.dataset.side = 'above'
  }, [open])

  if (!entry) return children

  return (
    <span ref={wrap} className={`term${fresh ? ' is-new' : ''}${chip ? ' term--chip' : ''}`}>
      <button
        type="button"
        className="term__word"
        aria-expanded={open}
        aria-controls={open ? popId : undefined}
        onClick={() => setOpen((v) => !v)}
      >
        {children}
      </button>
      {open && (
        <span ref={pop} id={popId} className="term__pop" role="note">
          {fresh && (
            <span className="term__new">New word</span>
          )}
          <span className="term__name">{entry.term}</span>
          <span className="term__def">{entry.definition}</span>
          {entry.example && <span className="term__example">{entry.example}</span>}
        </span>
      )}
    </span>
  )
}
