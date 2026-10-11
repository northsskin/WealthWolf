// Geometric wolf head. Colours come from the --wolf-* tokens so the mark
// follows the theme; `mono` paints it in one ink (currentColor) for stamps.
// `size` is a step on the mark scale in tokens.css: xs, sm, md, lg, xl.
export default function WolfMark({ size = 'md', mono = false, className = '', title }) {
  const fill = (token) => (mono ? 'currentColor' : `var(${token})`)
  const knockout = mono ? 'var(--paper)' : undefined
  return (
    <svg
      className={`wolfmark wolfmark--${size} ${className}`}
      viewBox="0 0 64 64"
      role={title ? 'img' : undefined}
      aria-hidden={title ? undefined : true}
      aria-label={title}
    >
      <polygon
        fill={fill('--wolf-head')}
        points="10,4 25,17 39,17 54,4 55,26 62,37 47,44 39,57 32,61 25,57 17,44 2,37 9,26"
      />
      {!mono && (
        <polygon fill="#000" opacity="0.16" points="32,17 39,17 54,4 55,26 62,37 47,44 39,57 32,61" />
      )}
      <polygon fill={knockout ?? 'var(--wolf-ear)'} points="12,9 22,19 13,24" />
      <polygon fill={knockout ?? 'var(--wolf-ear)'} points="52,9 42,19 51,24" />
      {!mono && (
        <polygon fill="var(--wolf-blaze)" opacity="0.5" points="32,20 38,30 36,48 32,52 28,48 26,30" />
      )}
      <polygon fill={knockout ?? 'var(--wolf-eye)'} points="17,31 27,33 20,36" />
      <polygon fill={knockout ?? 'var(--wolf-eye)'} points="47,31 37,33 44,36" />
      <polygon fill={knockout ?? 'var(--wolf-nose)'} points="28,49 36,49 32,54" />
    </svg>
  )
}
