import { h } from 'vue'
import type { Theme } from 'vitepress'
import DefaultTheme from 'vitepress/theme'
import './style.css'
import HomeHero from './components/HomeHero.vue'
import FeatureBook from './components/FeatureBook.vue'
import BookGrid from './components/BookGrid.vue'
import PostList from './components/PostList.vue'
import PatentGrid from './components/PatentGrid.vue'

export default {
  extends: DefaultTheme,
  Layout: () => h(DefaultTheme.Layout, null, {}),
  enhanceApp({ app }) {
    app.component('HomeHero', HomeHero)
    app.component('FeatureBook', FeatureBook)
    app.component('BookGrid', BookGrid)
    app.component('PostList', PostList)
    app.component('PatentGrid', PatentGrid)
  },
} satisfies Theme
