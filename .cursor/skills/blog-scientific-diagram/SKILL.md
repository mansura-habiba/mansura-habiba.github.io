---
name: blog-scientific-diagram
description: >-
  Creates a scientific explanatory diagram for a blog post and embeds it as an
  AnnotatedFigure. Use when a post needs a scientific diagram, a topic figure,
  a reference-architecture drawing, or a diagram that teaches the section's
  claim. Use the sequence layout only when the post explains the order of an
  exchange.
---

# Scientific diagrams for blog posts

The figure teaches one claim from the post. Draw a layered explanatory diagram: colored bands, the layer name, chips for the parts, arrows downward, and a return path when the topic loops. Use the sequence layout only when the claim is the order of an exchange among actors.

Do not hand-draw the SVG. Render it with the script in this skill, then put it in the post.

## Workflow

1. Write the claim in one sentence. That sentence is the figure title and the `AnnotatedFigure` caption.
2. Choose the composition.
   - `explanatory` for a mechanism, an architecture, or a topic the reader should see as layers. Schema in [reference.md](reference.md). The style example is `examples/secure-ai-reference-architecture.json`.
   - `sequence` when the post is about who did what, in order. The incident palette and lifeline layout are in [reference.md](reference.md).
3. Render:

```bash
python3 "<skill-dir>/scripts/render_figure.py" \
  path/to/spec.json \
  -o public/figures/<slug>.svg
```

`<skill-dir>` is the directory that contains this `SKILL.md`. The script exits non-zero when the canvas, type, or palette drifts.

4. Embed it in the post. The notice says what the reader should see.

```md
<AnnotatedFigure
  :number="1"
  caption="The claim, in one sentence."
  notice="The relation that makes the claim true.">

<img src="/figures/<slug>.svg" alt="The claim, in one sentence." />

</AnnotatedFigure>
```

5. Read the rendered figure. A reader who sees only the image should be able to restate the claim. Bands read top to bottom. Chips stay inside their band. The return arrow, when present, meets the band it names.

## Canvas

- Width `17.5cm` (a double column). The inset on every side is 10% of that width.
- White background. Sans-serif (Arial, Helvetica). No gradients, no shadows, no 3D.
- Figure title 12pt bold. Layer titles 10pt bold. Chips and flow labels stay at or under 10pt.
- Each layer uses one flat tone: blue, green, purple, teal, amber, or orange. Borders are solid. Arrowheads are filled triangles.
- Sequence figures keep the incident palette: black for the ordinary path, blue `#0066CC` for the failure path, yellow `#F4B400` for the incident span, and red `#FF0000` only on the label `Missing Retrieval Gate`.
