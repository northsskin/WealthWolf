import { useCallback, useRef, useState } from 'react'
import { Link, useNavigate } from 'react-router'
import { LogOut, UserRound } from 'lucide-react'
import ThemeToggle from './ThemeToggle.jsx'
import { useAuth } from '../lib/auth.js'
import { signOutAndReset, useSyncStatus } from '../lib/sync.js'
import { useDismiss } from '../lib/useDismiss.js'
import './AccountMenu.css'

const SYNC_COPY = {
  idle: 'Connecting…',
  connecting: 'Loading your account…',
  saving: 'Saving…',
  saved: 'Saved to your account',
  offline: 'Offline. Saves when you’re back.',
  error: 'Couldn’t save. Tries again on your next answer.',
}

// The account button in the header: your photo or initial when signed in, a
// plain user icon for guests. Theme lives in here too, to keep the header narrow.
export default function AccountMenu() {
  const { status, user } = useAuth()
  const sync = useSyncStatus()
  const navigate = useNavigate()
  const [open, setOpen] = useState(false)
  const [leaving, setLeaving] = useState(false)
  const ref = useRef(null)
  const close = useCallback(() => setOpen(false), [])
  useDismiss(ref, open, close)

  if (status === 'loading') return <span className="acctbtn acctbtn--loading" aria-hidden="true" />

  const signedIn = status === 'user'
  const initial = (user?.name || user?.email || '?')[0].toUpperCase()

  async function signOut() {
    setLeaving(true)
    try {
      await signOutAndReset()
      navigate('/')
    } finally {
      setLeaving(false)
    }
  }

  return (
    <div className="acctmenu" ref={ref}>
      <button
        className={signedIn ? 'acctbtn acctbtn--user' : 'acctbtn'}
        aria-expanded={open}
        aria-label={signedIn ? `Account: ${user.name || user.email}` : 'Account and settings'}
        onClick={() => setOpen((v) => !v)}
      >
        {signedIn && user.photoURL && <img src={user.photoURL} alt="" referrerPolicy="no-referrer" />}
        {signedIn && !user.photoURL && <span className="acctbtn__initial">{initial}</span>}
        {!signedIn && <UserRound />}
      </button>

      {open && (
        <div className="acctmenu__pop" role="dialog" aria-label="Account">
          {signedIn ? (
            <>
              <p className="acctmenu__name">{user.name || 'Signed in'}</p>
              <p className="acctmenu__email">{user.email}</p>
              <p className={`acctmenu__sync acctmenu__sync--${sync}`} role="status">
                {SYNC_COPY[sync]}
              </p>
            </>
          ) : (
            <>
              <p className="acctmenu__name">Not signed in</p>
              <p className="acctmenu__copy">
                Your progress lives only in this browser. An account keeps it safe and takes it to any device.
              </p>
              <div className="acctmenu__actions">
                <Link to="/signup" className="btn btn--block">
                  Create account
                </Link>
                <Link to="/signin" className="btn btn--ghost btn--block">
                  Sign in
                </Link>
              </div>
            </>
          )}

          <div className="acctmenu__row">
            <span>Theme</span>
            <ThemeToggle />
          </div>

          {signedIn && (
            <button className="btn btn--ghost btn--block acctmenu__out" onClick={signOut} disabled={leaving}>
              <LogOut /> {leaving ? 'Signing out…' : 'Sign out'}
            </button>
          )}
        </div>
      )}
    </div>
  )
}
