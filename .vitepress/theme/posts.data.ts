import { createContentLoader } from 'vitepress'

export interface Post {
  url: string
  title: string
  subtitle?: string
  date: string
  dateISO: string
  categories: string[]
  excerpt?: string
}

export default createContentLoader('blog/posts/*.md', {
  excerpt: true,
  transform(raw): Post[] {
    return raw
      .map(({ url, frontmatter, excerpt }) => {
        const isoDate: string = frontmatter.date
          ? new Date(frontmatter.date).toISOString()
          : new Date().toISOString()
        const human = new Date(isoDate).toLocaleDateString('en-US', {
          year: 'numeric',
          month: 'short',
          day: 'numeric',
        })
        return {
          url,
          title: frontmatter.title ?? '(untitled)',
          subtitle: frontmatter.subtitle,
          date: human,
          dateISO: isoDate,
          categories: Array.isArray(frontmatter.categories)
            ? frontmatter.categories
            : frontmatter.categories
            ? [frontmatter.categories]
            : [],
          excerpt: excerpt?.replace(/<[^>]+>/g, '').slice(0, 240),
        }
      })
      .sort((a, b) => +new Date(b.dateISO) - +new Date(a.dateISO))
  },
})
