import RichText from '../../Rich.jsx'

// The money story a story lesson opens with.
export default function StoryStep({ card }) {
  const { title, character, body } = card.step
  return (
    <article className="story">
      {character && <p className="eyebrow story__who">{character}</p>}
      <h2 className="display story__title">{title}</h2>
      <div className="story__body">
        <RichText text={body} />
      </div>
    </article>
  )
}

// Folded copy of the story above each of its questions.
export function StoryRecall({ story }) {
  return (
    <details className="recall">
      <summary>Re-read {story.character ? `${story.character.split(',')[0]}'s` : 'the'} story</summary>
      <div className="recall__body">
        <RichText text={story.body} />
      </div>
    </details>
  )
}
