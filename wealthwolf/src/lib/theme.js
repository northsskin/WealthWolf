import { useLayoutEffect } from 'react'
import { useStore } from '../store/store.js'

const THEME_COLOR = { light: '#ffffff', dark: '#0a0f1c' }

// Saves from before the toggle existed have no theme: they get light.
export function useTheme() {
  return useStore((s) => (s.settings.theme === 'dark' ? 'dark' : 'light'))
}

// Mirrors the saved theme onto <html> (index.html does the same before first paint).
export function useApplyTheme() {
  const theme = useTheme()
  useLayoutEffect(() => {
    const root = document.documentElement
    if (theme === 'dark') root.dataset.theme = 'dark'
    else delete root.dataset.theme
    document.querySelector('meta[name="theme-color"]')?.setAttribute('content', THEME_COLOR[theme])
  }, [theme])
}
