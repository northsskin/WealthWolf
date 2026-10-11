import Stamp from '../Stamp.jsx'
import { formatTime, ReceiptLine } from './LessonComplete.jsx'
import './shared.css'
import './LessonComplete.css'

export default function TrialFailed({ stats, onRetry, onLeave }) {
  return (
    <div className="done done--failed">
      <main className="done__main">
        <section className="receipt" aria-labelledby="failed-title">
          <header className="receipt__head">
            <p className="eyebrow">Den Trial receipt</p>
            <h1 id="failed-title" className="display done__title">
              Trial failed.
            </h1>
            <p className="done__sub">Three strikes. The den doesn’t forgive, but it does let you come back.</p>
          </header>
          <dl className="receipt__lines">
            <ReceiptLine label="Accuracy" value={`${stats.accuracy}%`} />
            <ReceiptLine label="Time" value={formatTime(stats.seconds)} />
            <ReceiptLine label="XP" value="+0" note="Pass the trial to collect it." />
          </dl>
          <p className="done__hint">Sharpen Up drills exactly the questions you keep missing. Try it before the next attempt.</p>
          <Stamp text="Not passed · Not passed · " tone="red" className="receipt__stamp" delay={400} tilt={8} />
        </section>
      </main>
      <footer className="fb">
        <div className="fb__inner">
          <button className="btn btn--ghost fb__btn" onClick={onLeave}>
            Back to path
          </button>
          <button className="btn fb__btn" onClick={onRetry} autoFocus>
            Try again
          </button>
        </div>
      </footer>
    </div>
  )
}
