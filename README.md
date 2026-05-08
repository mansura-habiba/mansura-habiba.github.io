# mansura-habiba.github.io

Personal site for **Mansura Habiba, Ph.D.** — Principal Platform Architect, AI &amp; HPC.
Built with [VitePress](https://vitepress.dev) and deployed to GitHub Pages via Actions.

## One-time setup after pushing

GitHub Pages must be set to deploy via Actions (not from a branch):

1. Go to **Settings → Pages**.
2. Under **Build and deployment → Source**, choose **GitHub Actions**.
3. Push to `main`. The `Deploy VitePress site to Pages` workflow will run on every push.

## Site map

| URL                 | Source                                      | What it is                                          |
| ------------------- | ------------------------------------------- | --------------------------------------------------- |
| `/`                 | `index.md`                                  | Landing page — hero, featured book, recent posts.   |
| `/about`            | `about.md`                                  | Short bio + link to full CV + contact.              |
| `/blog/`            | `blog/index.md` + `blog/posts/*.md`         | Blog index. Posts auto-listed via a data loader.    |
| `/book`             | `book.md`                                   | Three published books (data in `BookGrid.vue`).     |
| `/publications`     | `publications.md`                           | Patents, journals, conferences, talks.              |
| `/cv.html`          | `public/cv.html`                            | Full styled CV — original look preserved.           |
| `/cv-print.html`    | auto-generated from `public/cv.tex`         | Plain pandoc fallback (text-only).                  |

## Project structure

```
.
├── .vitepress/
│   ├── config.mts                      Site config, nav, head tags, GA
│   └── theme/
│       ├── index.ts                    Theme entry — registers components
│       ├── style.css                   Teal palette + custom layout styles
│       ├── posts.data.ts               Build-time loader for blog/posts/*.md
│       └── components/
│           ├── HomeHero.vue            Big hero on the homepage
│           ├── FeatureBook.vue         "Latest book" promo
│           ├── BookGrid.vue            Three-card book grid
│           ├── PostList.vue            Blog post list
│           └── PatentGrid.vue          Patent tile grid
├── public/                             Static assets — copied as-is to /
│   ├── cv.html                         The full styled CV
│   ├── cv.tex                          LaTeX source for the CV
│   ├── styles2.css                     Original CV stylesheet
│   ├── swiper-bundle.min.css           Swiper CSS used by the CV
│   ├── images/                         Photos
│   └── .nojekyll                       Stops GitHub Pages running Jekyll on output
├── index.md                            Homepage
├── about.md                            About page
├── book.md                             Books page
├── publications.md                     Publications page
├── blog/
│   ├── index.md                        Blog index page
│   └── posts/                          Blog posts (one .md per post)
├── package.json
└── .github/workflows/
    ├── deploy.yml                      Build VitePress + deploy to Pages
    └── latex-to-html.yml               Pandoc cv.tex → cv-print.html (no clobber)
```

## Run locally

You need Node 18+ (Node 20 LTS recommended).

```sh
npm install               # one-time
npm run dev               # http://localhost:5173 — hot reload
npm run build             # production build → .vitepress/dist
npm run preview           # serve the production build for sanity checking
```

## Adding a blog post

Drop a Markdown file into `blog/posts/`:

```text
blog/posts/2026-05-15-my-new-post.md
```

```yaml
---
title: My new post
subtitle: A short one-line summary.
date: 2026-05-15
categories: [agentic-ai, security]
---

# My new post

Body here…
```

It'll auto-appear in:
- the blog index (`/blog/`)
- the homepage's "Recent writing" list (newest 4)
- the build-time data loader (`.vitepress/theme/posts.data.ts`)

## Updating the CV

Two paths, depending on what you want to change:

1. **Visual / styled CV** at `/cv.html` — edit `public/cv.html` directly. Keep the
   small site-wide toolbar at the top intact.
2. **LaTeX source** at `/cv.tex` — edit `public/cv.tex`. When pushed to `main`,
   the `Convert LaTeX to HTML` action runs pandoc and writes
   `public/cv-print.html` (plain-text fallback). It does **not** overwrite
   `public/cv.html`.

## Updating books / patents

Both lists are static data inside Vue components — much simpler than markdown
hand-editing for repeated card layouts:

- Books: edit the `books` array in `.vitepress/theme/components/BookGrid.vue`.
- Patents: edit the `patents` array in `.vitepress/theme/components/PatentGrid.vue`.

## Design notes

- Body font: **Poppins** (matches the original CV).
- Display font: **Lora** (serif, gives the new pages a slightly more editorial
  feel while staying compatible with the CV's identity).
- Palette: same teal hue (HSL 173) as the CV, exposed as VitePress brand
  variables in `.vitepress/theme/style.css` so a single hue change re-skins
  the entire site.
