# Blog diagram specs

Input to `scripts/render_figure.py`. Unknown keys are rejected.

## Explanatory

Layered topic figure. `kind` is `band`, `flow`, or `split`. Order in `layers` is top to bottom. A downward arrow is drawn between consecutive layers. `return` draws the upward rail on the right.

```json
{
  "composition": "explanatory",
  "title": "Secure AI Reference Architecture",
  "layers": [
    {
      "kind": "band",
      "id": "governance",
      "title": "Governance & Obligation",
      "tone": "blue",
      "icon": "shield",
      "chips": ["Regulation", "Policy", "Risk", "System Registry"]
    },
    {
      "kind": "flow",
      "id": "execution",
      "title": "Execution",
      "tone": "purple",
      "icon": "chip",
      "source": "AI / Agent",
      "lanes": [
        ["Model Gateway", "Model / AI Service"],
        ["Tool Gateway", "Enterprise Tool"]
      ],
      "sink": "Workflow"
    },
    {
      "kind": "split",
      "columns": [
        {"id": "data", "title": "Data / Context", "tone": "teal", "icon": "database", "chips": ["Provenance", "Lineage"]},
        {"id": "runtime", "title": "Runtime Control", "tone": "amber", "icon": "sliders", "chips": ["Policy", "Limits"]}
      ]
    }
  ],
  "return": {"from": "runtime", "to": "governance"}
}
```

| Field | Rule |
| --- | --- |
| `tone` | `blue`, `green`, `purple`, `teal`, `amber`, `orange`. One flat fill and a matching border and title. |
| `icon` | Optional. `shield`, `key`, `chip`, `database`, `sliders`, `clipboard`, `search`. |
| `chips` | Short labels on a `band`. They must fit one row. |
| `lanes` | A `flow` layer. Each lane is two labels between `source` and `sink`. |
| `split` | Two bands side by side. Arrows drop from each column into the next layer. |
| `return` | Optional. `from` and `to` are layer ids. |

The full house-style example is `examples/secure-ai-reference-architecture.json`.

## Sequence

Use this when the blog claim is the order of an exchange. Actors sit on the top row. Time runs downward. Lifelines are dashed.

Palette for this composition only:

- Background `#FFFFFF`
- Ordinary path `#000000`
- Failure path `#0066CC`
- Incident span `#F4B400`
- `Missing Retrieval Gate` only: `#FF0000`
- Text and rounded-rectangle borders `#000000`

Canvas is `17.5cm` by `9.84375cm` (16:9), with 10% margins. Title 12pt bold. Interaction labels and times 10pt. Arrowheads are filled triangles. Rounded rectangles have a 2px black border.

```json
{
  "composition": "sequence",
  "title": "Ungrounded answer after a missing retrieval gate",
  "actors": [
    {"id": "customer", "name": "Customer (Mexico)"},
    {"id": "index", "name": "Vector Index (Shared)"},
    {"id": "model", "name": "Model"}
  ],
  "events": [
    {"kind": "message", "from": "customer", "to": "model", "label": "Query", "path": "standard", "time": "t0"},
    {"kind": "missing_retrieval_gate", "between": ["index", "model"], "time": "t1"},
    {"kind": "message", "from": "model", "to": "customer", "label": "Ungrounded answer", "path": "failure", "time": "t2"}
  ],
  "incident": {"label": "Incident", "start": 1, "end": 2}
}
```

`missing_retrieval_gate` prints `Missing Retrieval Gate`. At most one. Omit it, and omit red, when the post has no missing retrieval gate. A worked file is `examples/missing-retrieval-gate-sequence.json`.
