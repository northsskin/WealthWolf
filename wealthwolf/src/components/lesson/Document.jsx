import { Fragment } from 'react'
import PenMark from '../PenMark.jsx'
import { formatMoney } from '../../lib/session.js'
import './Document.css'

// Lines grouped under their section headings (Earnings, Deductions…), in order.
function sections(lines) {
  const out = []
  for (const line of lines) {
    const last = out[out.length - 1]
    if (last && last.name === (line.section ?? null)) last.lines.push(line)
    else out.push({ name: line.section ?? null, lines: [line] })
  }
  return out
}

function LineBody({ line }) {
  return (
    <>
      {line.date && <span className="figure doc__date">{line.date}</span>}
      <span className="doc__label">
        {line.qty && <span className="figure doc__qty">{line.qty} ×</span>}
        {line.label}
      </span>
      <span className="figure doc__amount">{formatMoney(line.amount, { cents: true })}</span>
    </>
  )
}

// A bill, pay stub, receipt or statement, drawn on the ledger. In `interactive`
// mode (spot the problem) every line is a button; after checking, the right line
// gets a green pen circle and a wrong pick gets struck through in red.
export default function Document({ doc, interactive = false, picked = null, revealed = false, answer, onPick }) {
  const due = doc.meta?.find(([label]) => /due/i.test(label))
  const meta = doc.meta?.filter((m) => m !== due) ?? []

  return (
    <figure className={`doc doc--${doc.kind}`} aria-label={`${doc.title}${doc.subtitle ? `, ${doc.subtitle}` : ''}`}>
      <header className="doc__head">
        <div>
          <p className="display doc__title">{doc.title}</p>
          {doc.subtitle && <p className="eyebrow doc__subtitle">{doc.subtitle}</p>}
        </div>
        {due && (
          <p className="doc__due">
            <span className="eyebrow">{due[0]}</span>
            <span className="figure">{due[1]}</span>
          </p>
        )}
      </header>

      {meta.length > 0 && (
        <dl className="doc__meta">
          {meta.map(([label, value]) => (
            <div key={label}>
              <dt>{label}</dt>
              <dd className="figure">{value}</dd>
            </div>
          ))}
        </dl>
      )}

      <div className="doc__lines" role={interactive ? 'radiogroup' : undefined} aria-label={interactive ? 'Lines on the document' : undefined}>
        {sections(doc.lines).map((section, i) => (
          <Fragment key={section.name ?? i}>
            {section.name && <p className="eyebrow doc__section">{section.name}</p>}
            {section.lines.map((line) => {
              if (!interactive) {
                return (
                  <div key={line.id} className="doc__line">
                    <LineBody line={line} />
                  </div>
                )
              }
              let state = picked === line.id ? 'is-picked' : ''
              if (revealed && line.id === answer) state = 'is-correct'
              else if (revealed && line.id === picked) state = 'is-wrong'
              return (
                <button
                  key={line.id}
                  type="button"
                  role="radio"
                  aria-checked={picked === line.id}
                  className={`doc__line doc__line--pick ${state}`}
                  onClick={() => onPick(line.id)}
                  disabled={revealed}
                >
                  <LineBody line={line} />
                  {state === 'is-correct' && <PenMark kind="ring" tone="green" className="doc__pen-circle" />}
                  {state === 'is-wrong' && <PenMark kind="strike" className="doc__pen-strike" />}
                </button>
              )
            })}
          </Fragment>
        ))}
      </div>

      {doc.totals?.length > 0 && (
        <div className="doc__totals">
          {doc.totals.map((total) => (
            <p key={total.label} className={total.strong ? 'doc__total is-strong' : 'doc__total'}>
              <span>{total.label}</span>
              <span className="figure">{formatMoney(total.amount, { cents: true })}</span>
            </p>
          ))}
        </div>
      )}

      {doc.note && <figcaption className="doc__note">{doc.note}</figcaption>}
    </figure>
  )
}

export function Documents({ docs }) {
  return (
    <div className={docs.length > 1 ? 'docs docs--pair' : 'docs'}>
      {docs.map((doc) => (
        <Document key={doc.title} doc={doc} />
      ))}
    </div>
  )
}
