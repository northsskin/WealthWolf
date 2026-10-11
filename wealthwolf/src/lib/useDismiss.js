import { useEffect } from 'react'

// Calls onDismiss on Escape or a pointer press outside `ref` while `active`.
export function useDismiss(ref, active, onDismiss) {
  useEffect(() => {
    if (!active) return
    function onPointer(event) {
      if (ref.current && !ref.current.contains(event.target)) onDismiss()
    }
    function onKey(event) {
      if (event.key === 'Escape') onDismiss()
    }
    document.addEventListener('pointerdown', onPointer)
    document.addEventListener('keydown', onKey)
    return () => {
      document.removeEventListener('pointerdown', onPointer)
      document.removeEventListener('keydown', onKey)
    }
  }, [ref, active, onDismiss])
}
