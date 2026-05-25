import { h } from 'vue'
import type { Theme } from 'vitepress'
import DefaultTheme from 'vitepress/theme'
import './style.css'
import './sdd-plus-doc.css'
import HomeHero from './components/HomeHero.vue'
import FeatureBook from './components/FeatureBook.vue'
import BookGrid from './components/BookGrid.vue'
import PostList from './components/PostList.vue'
import PatentGrid from './components/PatentGrid.vue'

// Long-form blog engagement blocks — drop-in patterns for posts that go
// past 1500 words and need rhythm changes beyond a single mermaid diagram.
import TldrCard from './components/TldrCard.vue'
import PullQuote from './components/PullQuote.vue'
import CrossIndustry from './components/CrossIndustry.vue'
import FailureMode from './components/FailureMode.vue'
import Principle from './components/Principle.vue'
import PrincipleList from './components/PrincipleList.vue'
import BeforeAfter from './components/BeforeAfter.vue'
import AnnotatedFigure from './components/AnnotatedFigure.vue'
import AsideNote from './components/AsideNote.vue'
import StopAndAsk from './components/StopAndAsk.vue'
import PartDivider from './components/PartDivider.vue'

export default {
  extends: DefaultTheme,
  Layout: () => h(DefaultTheme.Layout, null, {}),
  enhanceApp({ app }) {
    app.component('HomeHero', HomeHero)
    app.component('FeatureBook', FeatureBook)
    app.component('BookGrid', BookGrid)
    app.component('PostList', PostList)
    app.component('PatentGrid', PatentGrid)

    // Blog blocks
    app.component('TldrCard', TldrCard)
    app.component('PullQuote', PullQuote)
    app.component('CrossIndustry', CrossIndustry)
    app.component('FailureMode', FailureMode)
    app.component('Principle', Principle)
    app.component('PrincipleList', PrincipleList)
    app.component('BeforeAfter', BeforeAfter)
    app.component('AnnotatedFigure', AnnotatedFigure)
    app.component('AsideNote', AsideNote)
    app.component('StopAndAsk', StopAndAsk)
    app.component('PartDivider', PartDivider)
  },
} satisfies Theme
