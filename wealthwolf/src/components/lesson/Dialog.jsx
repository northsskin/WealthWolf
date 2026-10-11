import { useEffect, useId } from 'react'
import './Dialog.css'

export default function Dialog({ icon, title, children, actions, onEscape }) {
  const titleId = useId()

  useEffect(() => {
    if (!onEscape) return
    const onKey = (event) => event.key === 'Escape' && onEscape()
    window.addEventListener('keydown', onKey)
    return () => window.removeEventListener('keydown', onKey)
  }, [onEscape])

  return (
    <div className="dialog__scrim">
      <div className="dialog" role="dialog" aria-modal="true" aria-labelledby={titleId}>
        {icon && <div className="dialog__icon">{icon}</div>}
        <h2 id={titleId} className="dialog__title">
          {title}
        </h2>
        <div className="dialog__body">{children}</div>
        <div className="dialog__actions">{actions}</div>
      </div>
    </div>
  )
}
