import Logo from './Logo.jsx'
import './Bar.css'

// The one header every screen outside a lesson uses: logo left, actions right.
export default function Bar({ children, sticky = false }) {
  return (
    <header className={sticky ? 'bar bar--sticky' : 'bar'}>
      <div className="bar__inner">
        <Logo />
        <div className="bar__actions">{children}</div>
      </div>
    </header>
  )
}
