import { Moon, Sun } from 'lucide-react'
import { actions } from '../store/store.js'
import { useTheme } from '../lib/theme.js'
import './ThemeToggle.css'

export default function ThemeToggle() {
  const dark = useTheme() === 'dark'
  const label = dark ? 'Switch to light mode' : 'Switch to dark mode'
  return (
    <button
      className="theme-toggle"
      onClick={() => actions.setTheme(dark ? 'light' : 'dark')}
      aria-label={label}
      aria-pressed={dark}
      title={label}
    >
      {dark ? <Sun /> : <Moon />}
    </button>
  )
}
