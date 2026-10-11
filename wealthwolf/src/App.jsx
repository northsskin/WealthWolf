import { useEffect } from 'react'
import { Navigate, Route, Routes } from 'react-router'
import Landing from './screens/Landing.jsx'
import Learn from './screens/Learn.jsx'
import Lesson from './screens/Lesson.jsx'
import Glossary from './screens/Glossary.jsx'
import WordDrill from './screens/WordDrill.jsx'
import Account from './screens/Account.jsx'
import { useApplyTheme } from './lib/theme.js'
import { useAuth } from './lib/auth.js'
import { startSync } from './lib/sync.js'

// While someone is signed in, their progress syncs with their account.
function useAccountSync() {
  const { status, user } = useAuth()
  const uid = status === 'user' ? user.uid : null
  useEffect(() => (uid ? startSync(uid) : undefined), [uid])
}

export default function App() {
  useApplyTheme()
  useAccountSync()
  return (
    <Routes>
      <Route path="/" element={<Landing />} />
      <Route path="/learn" element={<Learn />} />
      <Route path="/lesson/:lessonId" element={<Lesson />} />
      <Route path="/glossary" element={<Glossary />} />
      <Route path="/glossary/drill" element={<WordDrill />} />
      <Route path="/signup" element={<Account mode="signup" />} />
      <Route path="/signin" element={<Account mode="signin" />} />
      <Route path="*" element={<Navigate to="/" replace />} />
    </Routes>
  )
}
