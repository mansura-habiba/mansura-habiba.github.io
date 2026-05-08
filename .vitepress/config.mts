import { defineConfig } from 'vitepress'

// https://vitepress.dev/reference/site-config
export default defineConfig({
  title: 'Mansura Habiba',
  description:
    'Personal site for Mansura Habiba, Ph.D. — Principal Platform Architect for AI and HPC platforms. Writing on agentic AI security, hybrid cloud, and HPC architecture.',
  cleanUrls: true,
  lastUpdated: false,
  appearance: 'dark', // user can toggle; default to dark off
  ignoreDeadLinks: [
    // The styled CV is a static file in /public/cv.html — VitePress won't index it
    /^\/cv\.html/,
    /^\/cv-print\.html/,
    /^\/cv\.tex/,
  ],

  head: [
    ['link', { rel: 'icon', type: 'image/png', href: '/images/mansura.png' }],
    ['meta', { name: 'author', content: 'Mansura Habiba' }],
    ['meta', { property: 'og:type', content: 'website' }],
    ['meta', { property: 'og:site_name', content: 'Mansura Habiba' }],
    [
      'link',
      {
        rel: 'preconnect',
        href: 'https://fonts.googleapis.com',
      },
    ],
    [
      'link',
      {
        rel: 'preconnect',
        href: 'https://fonts.gstatic.com',
        crossorigin: '',
      },
    ],
    [
      'link',
      {
        rel: 'stylesheet',
        href: 'https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&family=Lora:ital,wght@0,400;0,500;0,600;1,400&display=swap',
      },
    ],
    // Google Analytics (preserved from original site)
    [
      'script',
      {
        async: '',
        src: 'https://www.googletagmanager.com/gtag/js?id=G-2367QRTG56',
      },
    ],
    [
      'script',
      {},
      `window.dataLayer = window.dataLayer || [];
       function gtag(){dataLayer.push(arguments);}
       gtag('js', new Date());
       gtag('config', 'G-2367QRTG56');`,
    ],
  ],

  themeConfig: {
    siteTitle: 'Mansura Habiba',
    logo: undefined,

    nav: [
      { text: 'Blog', link: '/blog/', activeMatch: '^/blog/' },
      { text: 'Books', link: '/book', activeMatch: '^/book' },
      { text: 'Publications', link: '/publications', activeMatch: '^/publications' },
      { text: 'About', link: '/about', activeMatch: '^/about' },
      { text: 'CV', link: '/cv.html', target: '_self', noIcon: true },
    ],

    // No sidebar — this is a portfolio, not docs.
    sidebar: false,
    aside: false,
    outline: false,
    docFooter: { prev: false, next: false },

    socialLinks: [
      { icon: 'github', link: 'https://github.com/mansura-habiba' },
      { icon: 'linkedin', link: 'https://www.linkedin.com/in/mansura-h-a0174a19' },
      { icon: 'twitter', link: 'https://twitter.com/MansuraHabiba' },
      {
        icon: {
          svg: '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path fill="currentColor" d="M2.846 6.887c.03-.295-.083-.586-.303-.784l-2.24-2.7v-.403h6.958l5.378 11.795 4.728-11.795H24v.403l-1.916 1.837c-.165.126-.247.333-.213.538v13.498c-.034.204.048.411.213.537l1.871 1.837v.403h-9.412v-.403l1.939-1.882c.19-.19.19-.246.19-.537V7.794L13.31 20.498h-.719L7.027 7.794v8.512c-.052.385.076.774.347 1.052l2.521 3.058v.404H2.732v-.404l2.521-3.058c.27-.279.39-.67.325-1.052V6.887z"/></svg>',
        },
        link: 'https://mansurahabiba.medium.com/',
        ariaLabel: 'Medium',
      },
    ],

    footer: {
      message:
        'Built with VitePress · Views are my own · <a href="/cv.html">Full CV</a>',
      copyright:
        '© ' +
        new Date().getFullYear() +
        ' Mansura Habiba',
    },

    search: {
      provider: 'local',
    },
  },
})
