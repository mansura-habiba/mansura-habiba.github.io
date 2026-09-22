# Session summary — blog scientific diagram skill (2026-09-22)

## Task

Name and shape the skill that draws scientific diagrams for posts on this site.

## Where it lives

- Skill: `.cursor/skills/blog-scientific-diagram/SKILL.md`
- Renderer: `.cursor/skills/blog-scientific-diagram/scripts/render_figure.py`
- Style example: `.cursor/skills/blog-scientific-diagram/examples/secure-ai-reference-architecture.json`
- Capability: [`../capability/blog-scientific-diagram.md`](../capability/blog-scientific-diagram.md)

## Decision

The skill is `blog-scientific-diagram`. The figure explains one claim in a post and is embedded with `AnnotatedFigure`. The default drawing is a layered architecture: a title, tinted bands, chips, arrows down the stack, and a return path when the topic loops. A sequence diagram is used only when the post is about the order of an exchange.

The layered example follows the Secure AI reference architecture the session used as the visual target. Width stays 17.5 cm. Each layer has one flat tone. The renderer rejects gradients, shadows, and colors outside that palette.
