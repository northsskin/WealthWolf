import RichText, { Rich } from '../../Rich.jsx'

export default function InfoStep({ card }) {
  const { title, body, callout } = card.step
  return (
    <div className="info">
      <h2 className="step__prompt info__title">
        <Rich text={title} />
      </h2>
      <div className="info__body">
        <RichText text={body} />
      </div>
      {callout && (
        <div className="info__callout">
          <span className="eyebrow">Remember</span>
          <p>
            <Rich text={callout} />
          </p>
        </div>
      )}
    </div>
  )
}
