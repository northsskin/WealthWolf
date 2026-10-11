import { useState } from 'react'
import { Link, Navigate, useSearchParams } from 'react-router'
import { Eye, EyeOff } from 'lucide-react'
import Bar from '../components/Bar.jsx'
import ThemeToggle from '../components/ThemeToggle.jsx'
import { ReceiptLine } from '../components/lesson/LessonComplete.jsx'
import { configured, usingEmulators } from '../lib/firebase.js'
import { friendlyError, sendReset, signInWithEmail, signInWithGoogle, signUpWithEmail, useAuth } from '../lib/auth.js'
import { liveStreak, useStore } from '../store/store.js'
import './Account.css'

// Only paths on this site, so ?next= can't send anyone somewhere else.
const safeNext = (value) => (value?.startsWith('/') && !value.startsWith('//') ? value : '/learn')

const fail = (code) => Object.assign(new Error(code), { code })

export default function Account({ mode }) {
  const signup = mode === 'signup'
  const [params] = useSearchParams()
  const next = safeNext(params.get('next'))
  const { status } = useAuth()
  const xp = useStore((s) => s.xp)
  const words = useStore((s) => Object.keys(s.terms).length)
  const streak = useStore((s) => liveStreak(s.streak))

  const [name, setName] = useState('')
  const [email, setEmail] = useState('')
  const [password, setPassword] = useState('')
  const [showPassword, setShowPassword] = useState(false)
  const [busy, setBusy] = useState(null) // which button is waiting: google | email | reset
  const [error, setError] = useState(null)
  const [notice, setNotice] = useState(null)

  // Signed in (just now, or already): carry on to wherever they were headed.
  if (status === 'user') return <Navigate to={next} replace />

  const saving = signup && xp > 0
  const switchTo = `${signup ? '/signin' : '/signup'}${params.size ? `?${params}` : ''}`

  async function run(kind, task) {
    setBusy(kind)
    setError(null)
    setNotice(null)
    try {
      await task()
    } catch (err) {
      setError(friendlyError(err))
    } finally {
      setBusy(null)
    }
  }

  function submit(event) {
    event.preventDefault()
    run('email', () => {
      if (!email.trim()) throw fail('auth/missing-email')
      if (!password) throw fail('auth/missing-password')
      return signup ? signUpWithEmail(name, email, password) : signInWithEmail(email, password)
    })
  }

  function forgot() {
    run('reset', async () => {
      if (!email.trim()) throw fail('auth/missing-email')
      await sendReset(email)
      setNotice('If there’s an account for that email, a reset link is on its way.')
    })
  }

  let eyebrow, title, sub
  if (saving) {
    eyebrow = 'Save your progress'
    title = 'Keep what you’ve earned.'
    sub = 'Make a free account to keep your XP, streak and words, and unlock the rest of the path.'
  } else if (signup) {
    eyebrow = 'New account'
    title = 'Create your account.'
    sub = 'It’s free. Your progress saves to it, so it follows you to any device.'
  } else {
    eyebrow = 'Welcome back'
    title = 'Sign in.'
    sub = 'Pick up where you left off, on this device or any other.'
  }

  return (
    <div className="acct">
      <Bar>
        <ThemeToggle />
      </Bar>

      <main className="acct__main">
        <section className="acct__sheet" aria-labelledby="acct-title">
          <p className="eyebrow">{eyebrow}</p>
          <h1 id="acct-title" className="display acct__title">
            {title}
          </h1>
          <p className="acct__sub">{sub}</p>

          {saving && (
            <dl className="receipt__lines acct__keep" aria-label="What you’ll keep">
              <ReceiptLine label="XP" value={xp} />
              <ReceiptLine label="Words learned" value={words} />
              <ReceiptLine label="Streak" value={`${streak} day${streak === 1 ? '' : 's'}`} />
            </dl>
          )}

          {!configured && (
            <p className="acct__setup" role="note">
              {import.meta.env.DEV ? (
                <>
                  Sign-in isn’t set up yet. Put the Firebase settings in <code>.env.local</code> (see{' '}
                  <code>.env.example</code>) and restart the dev server, or run <code>npm run dev:emu</code> to try
                  accounts on this computer only.
                </>
              ) : (
                'Sign-in is unavailable right now.'
              )}
            </p>
          )}

          <button
            type="button"
            className="acct__google"
            onClick={() => run('google', signInWithGoogle)}
            disabled={!configured || busy !== null}
          >
            <GoogleMark />
            {busy === 'google' ? 'Waiting for Google…' : 'Continue with Google'}
          </button>

          <p className="acct__or" aria-hidden="true">
            or
          </p>

          <form className="acct__form" onSubmit={submit} noValidate>
            {signup && (
              <label className="acct__field">
                <span className="eyebrow">Name</span>
                <span className="acct__input">
                  <input
                    value={name}
                    onChange={(event) => setName(event.target.value)}
                    autoComplete="name"
                    placeholder="What should the Wolf call you?"
                  />
                </span>
              </label>
            )}
            <label className="acct__field">
              <span className="eyebrow">Email</span>
              <span className="acct__input">
                <input
                  type="email"
                  value={email}
                  onChange={(event) => setEmail(event.target.value)}
                  autoComplete="email"
                  inputMode="email"
                  required
                />
              </span>
            </label>
            <label className="acct__field">
              <span className="eyebrow">Password</span>
              <span className="acct__input">
                <input
                  type={showPassword ? 'text' : 'password'}
                  value={password}
                  onChange={(event) => setPassword(event.target.value)}
                  autoComplete={signup ? 'new-password' : 'current-password'}
                  minLength={6}
                  required
                />
                <button
                  type="button"
                  className="acct__peek"
                  onClick={() => setShowPassword((v) => !v)}
                  aria-label={showPassword ? 'Hide password' : 'Show password'}
                  aria-pressed={showPassword}
                >
                  {showPassword ? <EyeOff /> : <Eye />}
                </button>
              </span>
              {signup && <span className="acct__hint">At least 6 characters.</span>}
            </label>

            {error && (
              <p className="acct__msg acct__msg--error" role="alert">
                {error}
              </p>
            )}
            {notice && (
              <p className="acct__msg acct__msg--ok" role="status">
                {notice}
              </p>
            )}

            <button type="submit" className="btn btn--lg btn--block acct__submit" disabled={!configured || busy !== null}>
              {busy === 'email' ? 'One moment…' : signup ? 'Create account' : 'Sign in'}
            </button>
          </form>

          <div className="acct__links">
            <span>
              {signup ? 'Already have an account?' : 'New here?'}{' '}
              <Link to={switchTo}>{signup ? 'Sign in' : 'Create an account'}</Link>
            </span>
            {!signup && (
              <button type="button" className="textbtn" onClick={forgot} disabled={!configured || busy !== null}>
                Forgot password?
              </button>
            )}
          </div>

          {usingEmulators && (
            <p className="acct__fine">Emulator mode: accounts here are test accounts on this computer only.</p>
          )}
        </section>
      </main>
    </div>
  )
}

// Google's "G", in the colours Google asks for on its sign-in buttons.
function GoogleMark() {
  return (
    <svg className="acct__g" viewBox="0 0 48 48" aria-hidden="true">
      <path
        fill="#EA4335"
        d="M24 9.5c3.54 0 6.71 1.22 9.21 3.6l6.85-6.85C35.9 2.38 30.47 0 24 0 14.62 0 6.51 5.38 2.56 13.22l7.98 6.19C12.43 13.72 17.74 9.5 24 9.5z"
      />
      <path
        fill="#4285F4"
        d="M46.98 24.55c0-1.57-.15-3.09-.38-4.55H24v9.02h12.94c-.58 2.96-2.26 5.48-4.78 7.18l7.73 6c4.51-4.18 7.09-10.36 7.09-17.65z"
      />
      <path
        fill="#FBBC05"
        d="M10.53 28.59c-.48-1.45-.76-2.99-.76-4.59s.27-3.14.76-4.59l-7.98-6.19C.92 16.46 0 20.12 0 24c0 3.88.92 7.54 2.56 10.78l7.97-6.19z"
      />
      <path
        fill="#34A853"
        d="M24 48c6.48 0 11.93-2.13 15.89-5.81l-7.73-6c-2.15 1.45-4.92 2.3-8.16 2.3-6.26 0-11.57-4.22-13.47-9.91l-7.98 6.19C6.51 42.62 14.62 48 24 48z"
      />
    </svg>
  )
}
