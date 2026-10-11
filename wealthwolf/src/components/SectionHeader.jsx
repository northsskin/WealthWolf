import { useCallback, useRef, useState } from 'react'
import { Check, ChevronDown } from 'lucide-react'
import { sections } from '../lib/content.js'
import { useDismiss } from '../lib/useDismiss.js'
import './SectionHeader.css'

// How far through a section the player is, counted in whole units.
export function sectionProgress(section, completed) {
  const unitsDone = section.units.filter((mod) => mod.lessons.every((l) => completed[l.id])).length
  const trialDone = !section.trial || Boolean(completed[section.trial.id])
  return { unitsDone, units: section.units.length, cleared: unitsDone === section.units.length && trialDone }
}

// The title page of a section, with a picker to jump to any other section.
export default function SectionHeader({ section, completed, currentSectionId, onPick }) {
  const [open, setOpen] = useState(false)
  const ref = useRef(null)
  const close = useCallback(() => setOpen(false), [])
  useDismiss(ref, open, close)
  const { unitsDone, units } = sectionProgress(section, completed)

  return (
    <header className="sechead">
      <div className="sechead__top">
        <p className="eyebrow sechead__no">
          Section {section.number} of {sections.length}
        </p>
        {sections.length > 1 && (
          <div className="sechead__picker" ref={ref}>
            <button className="sechead__toggle" aria-expanded={open} onClick={() => setOpen((v) => !v)}>
              All sections <ChevronDown />
            </button>
            {open && (
              <ol className="sechead__menu" aria-label="Sections">
                {sections.map((s) => {
                  const p = sectionProgress(s, completed)
                  return (
                    <li key={s.id}>
                      <button
                        className={s.id === section.id ? 'sechead__item is-shown' : 'sechead__item'}
                        aria-current={s.id === section.id ? 'true' : undefined}
                        onClick={() => {
                          onPick(s.id)
                          setOpen(false)
                        }}
                      >
                        <span className="figure sechead__item-no">{String(s.number).padStart(2, '0')}</span>
                        <span className="sechead__item-title">
                          {s.title}
                          {s.id === currentSectionId && <span className="sechead__here">You’re here</span>}
                        </span>
                        <span className="figure sechead__item-count">
                          {p.cleared ? <Check aria-label="Cleared" /> : `${p.unitsDone}/${p.units}`}
                        </span>
                      </button>
                    </li>
                  )
                })}
              </ol>
            )}
          </div>
        )}
      </div>
      <h1 className="display sechead__title">{section.title}</h1>
      <p className="sechead__desc">{section.description}</p>
      <div className="sechead__meter">
        <div
          className="sechead__bar"
          role="progressbar"
          aria-label={`${section.title} progress`}
          aria-valuemin={0}
          aria-valuemax={units}
          aria-valuenow={unitsDone}
        >
          <span style={{ width: `${(unitsDone / units) * 100}%` }} />
        </div>
        <span className="figure sechead__count">
          {unitsDone}/{units} units
        </span>
      </div>
    </header>
  )
}
