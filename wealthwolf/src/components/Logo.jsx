import { Link } from 'react-router'
import WolfMark from './WolfMark.jsx'
import './Logo.css'

export default function Logo({ to = '/' }) {
  return (
    <Link to={to} className="logo" aria-label="Wealthwolf home">
      <WolfMark size="sm" />
      <span className="logo__word">Wealthwolf</span>
    </Link>
  )
}
