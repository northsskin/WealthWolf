import { useEffect, useState } from 'react'
import { Link, Navigate, useSearchParams } from 'react-router'
import { Eye, EyeOff } from 'lucide-react'
import Bar from '../components/Bar.jsx'
import ThemeToggle from '../components/ThemeToggle.jsx'
import { ReceiptLine } from '../components/lesson/LessonComplete.jsx'
import { configured } from '../lib/supabase.js'
import {
  friendlyError,
  redirectError,
  sendReset,
  signInWithEmail,
  signInWithGoogle,
  signUpWithEmail,
  updatePassword,
  useAuth,
  useAuthSettings,
} from '../lib/auth.js'
import { liveStreak, useStore } from '../store/store.js'
import './Account.css'

// Only paths on this site, so ?next= can't send anyone somewhere else.
const safeNext = (value) => (value?.startsWith('/') && !value.startsWith('//') ? value : '/learn')

const fail = (code) => Object.assign(new Error(code), { code })

// /signup, /signin, and /reset-password (where a password-reset email lands).
export default function Account({ mode }) {
  return mode === 'reset' ? <ResetPassword /> : <SignInOrUp signup={mode === 'signup'} />
}

function Sheet({ children }) {
  return (
    <div className="acct">
      <Bar>
        <ThemeToggle />
      </Bar>
      <main className="acct__main">
        <section className="acct__sheet" aria-labelledby="acct-title">
          {children}
        </section>
      </main>
    </div>
  )
}

function Heading({ eyebrow, title, sub }) {
  return (
    <>
      <p className="eyebrow">{eyebrow}</p>
      <h1 id="acct-title" className="display acct__title">
        {title}
      </h1>
      {sub && <p className="acct__sub">{sub}</p>}
    </>
  )
}

function SignInOrUp({ signup }) {
  const [params] = useSearchParams()
  const next = safeNext(params.get('next'))
  const { status } = useAuth()
  const settings = useAuthSettings()
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
  const [sentTo, setSentTo] = useState(null) // address a confirmation email went to

  // Coming back from Google with an error (they cancelled, or something failed).
  useEffect(() => {
    const returned = redirectError()
    if (returned) setError(friendlyError({ code: returned.code }))
  }, [])

  // Signed in (just now, or already): carry on to wherever they were headed.
  if (status === 'user') return <Navigate to={next} replace />

  // Back from Google or an email link: Supabase is finishing the sign-in.
  if (status === 'loading' && params.has('code')) {
    return (
      <Sheet>
        <Heading eyebrow="One moment" title="Signing you in…" />
      </Sheet>
    )
  }

  // Google and email links come back here, then on to `next`.
  const returnTo = `${signup ? '/signup' : '/signin'}?next=${encodeURIComponent(next)}`
  const switchTo = `${signup ? '/signin' : '/signup'}${params.size ? `?${params}` : ''}`
  const googleOff = settings !== null && !settings.google
  const saving = signup && xp > 0

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
    run('email', async () => {
      if (!email.trim()) throw fail('missing_email')
      if (!password) throw fail('missing_password')
      if (!signup) return signInWithEmail(email, password)
      const { needsConfirmation } = await signUpWithEmail(name, email, password, returnTo)
      if (needsConfirmation) setSentTo(email.trim())
    })
  }

  function forgot() {
    run('reset', async () => {
      if (!email.trim()) throw fail('missing_email')
      await sendReset(email)
      setNotice('If there’s an account for that email, a reset link is on its way.')
    })
  }

  if (sentTo) {
    return (
      <Sheet>
        <Heading
          eyebrow="Almost there"
          title="Check your email."
          sub={`We sent a link to ${sentTo}. Open it on this device to finish creating your account${xp > 0 ? ', and your progress here will be saved to it' : ''}.`}
        />
        <p className="acct__fine">No email after a few minutes? Check your spam folder.</p>
        <div className="acct__links">
          <button type="button" className="textbtn" onClick={() => setSentTo(null)}>
            Use a different email
          </button>
        </div>
      </Sheet>
    )
  }

  let heading
  if (saving) {
    heading = { eyebrow: 'Save your progress', title: 'Keep what you’ve earned.',
      sub: 'Make a free account to keep your XP, streak and words, and unlock the rest of the path.' }
  } else if (signup) {
    heading = { eyebrow: 'New account', title: 'Create your account.', sub: 'It’s free. Your progress saves to it, so it follows you to any device.' }
  } else {
    heading = { eyebrow: 'Welcome back', title: 'Sign in.', sub: 'Pick up where you left off, on this device or any other.' }
  }

  return (
    <Sheet>
      <Heading {...heading} />

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
              Sign-in isn’t set up yet. The Supabase URL and publishable key belong in <code>.env</code> (see{' '}
              <code>.env.example</code>). Restart the dev server after adding them.
            </>
          ) : (
            'Sign-in is unavailable right now.'
          )}
        </p>
      )}

      <button
        type="button"
        className="acct__google"
        onClick={() => run('google', () => signInWithGoogle(returnTo))}
        disabled={!configured || busy !== null || googleOff}
      >
        <GoogleMark />
        {busy === 'google' ? 'Opening Google…' : 'Continue with Google'}
      </button>
      {googleOff && (
        <p className="acct__hint acct__google-off">
          Google sign-in isn’t switched on yet.
          {import.meta.env.DEV && ' Turn it on in Supabase under Authentication → Sign In / Providers → Google.'}
        </p>
      )}

      <p className="acct__or" aria-hidden="true">
        or
      </p>

      <form className="acct__form" onSubmit={submit} noValidate>
        {signup && (
          <label className="acct__field">
            <span className="eyebrow">Name</span>
            <span className="acct__input">
              <input value={name} onChange={(event) => setName(event.target.value)} autoComplete="name" placeholder="What should the Wolf call you?" />
            </span>
          </label>
        )}
        <label className="acct__field">
          <span className="eyebrow">Email</span>
          <span className="acct__input">
            <input type="email" value={email} onChange={(event) => setEmail(event.target.value)} autoComplete="email" inputMode="email" required />
          </span>
        </label>
        <PasswordField
          value={password}
          onChange={setPassword}
          show={showPassword}
          onToggle={() => setShowPassword((v) => !v)}
          autoComplete={signup ? 'new-password' : 'current-password'}
          hint={signup ? 'At least 6 characters.' : null}
        />

        <Messages error={error} notice={notice} />

        <button type="submit" className="btn btn--lg btn--block acct__submit" disabled={!configured || busy !== null}>
          {busy === 'email' ? 'One moment…' : signup ? 'Create account' : 'Sign in'}
        </button>
      </form>

      <div className="acct__links">
        <span>
          {signup ? 'Already have an account?' : 'New here?'} <Link to={switchTo}>{signup ? 'Sign in' : 'Create an account'}</Link>
        </span>
        {!signup && (
          <button type="button" className="textbtn" onClick={forgot} disabled={!configured || busy !== null}>
            Forgot password?
          </button>
        )}
      </div>
    </Sheet>
  )
}

// Where a password-reset email lands. The link has already signed them in.
function ResetPassword() {
  const { status } = useAuth()
  const [password, setPassword] = useState('')
  const [showPassword, setShowPassword] = useState(false)
  const [busy, setBusy] = useState(false)
  const [error, setError] = useState(null)
  const [done, setDone] = useState(false)

  if (status === 'loading') {
    return (
      <Sheet>
        <Heading eyebrow="One moment" title="Opening your reset link…" />
      </Sheet>
    )
  }
  if (status === 'guest') {
    return (
      <Sheet>
        <Heading eyebrow="Reset password" title="That link has expired." sub="Reset links work once and only for a short time. Ask for a new one from the sign-in page." />
        <div className="acct__links">
          <Link to="/signin">Back to sign in</Link>
        </div>
      </Sheet>
    )
  }
  if (done) {
    return (
      <Sheet>
        <Heading eyebrow="Reset password" title="Password changed." sub="You’re signed in with your new password." />
        <Link to="/learn" className="btn btn--lg btn--block acct__submit">
          Back to the path
        </Link>
      </Sheet>
    )
  }

  async function submit(event) {
    event.preventDefault()
    setBusy(true)
    setError(null)
    try {
      if (!password) throw fail('missing_password')
      await updatePassword(password)
      setDone(true)
    } catch (err) {
      setError(friendlyError(err))
    } finally {
      setBusy(false)
    }
  }

  return (
    <Sheet>
      <Heading eyebrow="Reset password" title="Choose a new password." />
      <form className="acct__form acct__form--spaced" onSubmit={submit} noValidate>
        <PasswordField
          value={password}
          onChange={setPassword}
          show={showPassword}
          onToggle={() => setShowPassword((v) => !v)}
          autoComplete="new-password"
          hint="At least 6 characters."
          label="New password"
        />
        <Messages error={error} />
        <button type="submit" className="btn btn--lg btn--block acct__submit" disabled={busy}>
          {busy ? 'One moment…' : 'Save new password'}
        </button>
      </form>
    </Sheet>
  )
}

function PasswordField({ value, onChange, show, onToggle, autoComplete, hint, label = 'Password' }) {
  return (
    <label className="acct__field">
      <span className="eyebrow">{label}</span>
      <span className="acct__input">
        <input type={show ? 'text' : 'password'} value={value} onChange={(event) => onChange(event.target.value)} autoComplete={autoComplete} minLength={6} required />
        <button type="button" className="acct__peek" onClick={onToggle} aria-label={show ? 'Hide password' : 'Show password'} aria-pressed={show}>
          {show ? <EyeOff /> : <Eye />}
        </button>
      </span>
      {hint && <span className="acct__hint">{hint}</span>}
    </label>
  )
}

function Messages({ error, notice }) {
  return (
    <>
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
    </>
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
