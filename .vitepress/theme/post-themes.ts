export const THEMES = [
  {
    label: 'Knowledge & data',
    tags: ['knowledge-architecture', 'accountable-knowledge', 'enterprise-ai', 'data', 'provenance'],
  },
  {
    label: 'Security & governance',
    tags: ['security', 'identity', 'governance', 'guardrails', 'ai-governance', 'certification', 'cryptography'],
  },
  {
    label: 'Engineering practice',
    tags: ['engineering', 'software development', 'sdlc', 'ai sdlc', 'sdd-plus', 'skills', 'verification'],
  },
  {
    label: 'Agent architecture',
    tags: ['strategy', 'orchestration', 'agentic pattern'],
  },
  {
    label: 'Quantum',
    tags: ['quantum', 'physics'],
  },
]

const FALLBACK_THEME = 'Agent architecture'

export function themesFor(categories: string[]): string[] {
  const tags = categories.map((c) => c.toLowerCase())
  const found = THEMES.filter((t) => t.tags.some((tag) => tags.includes(tag))).map((t) => t.label)
  return found.length ? found : [FALLBACK_THEME]
}
