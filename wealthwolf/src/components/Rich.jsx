import Term from './Term.jsx'
import { termId } from '../lib/content.js'

const TOKEN = /(\*\*.+?\*\*|\[\[[^\]]+\]\])/g
const LINK = /^\[\[([^\]|]+)(?:\|([^\]]+))?\]\]$/

// Inline content text: **bold** and [[term]] / [[display|term-id]] glossary links.
export function Rich({ text }) {
  if (!text) return null
  return text.split(TOKEN).map((part, i) => {
    if (part.length > 4 && part.startsWith('**') && part.endsWith('**')) {
      return (
        <strong key={i}>
          <Rich text={part.slice(2, -2)} />
        </strong>
      )
    }
    const link = part.match(LINK)
    if (link) {
      return (
        <Term key={i} id={link[2] ?? termId(link[1])}>
          {link[1]}
        </Term>
      )
    }
    return part
  })
}

// Block content text: blank lines split paragraphs.
export default function RichText({ text, className }) {
  return text.split('\n\n').map((paragraph, i) => (
    <p key={i} className={className}>
      <Rich text={paragraph} />
    </p>
  ))
}
