#!/usr/bin/env python3
"""Render a scientific diagram for a blog post.

composition "explanatory" is the layered topic figure.
composition "sequence" is the actor timeline, used when order is the claim.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import render_explanatory
import render_postmortem_sequence as sequence


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("spec", type=Path)
    parser.add_argument("-o", "--output", type=Path, required=True)
    args = parser.parse_args(argv)
    try:
        data = json.loads(args.spec.read_text())
        if not isinstance(data, dict):
            raise sequence.SpecError("spec must be a JSON object")
        composition = data.get("composition")
        if composition is None and "layers" in data:
            composition = "explanatory"
        if composition is None and "events" in data:
            composition = "sequence"
        if composition == "explanatory":
            spec = render_explanatory.load_spec(data)
            svg = render_explanatory.render(spec)
            render_explanatory.validate_svg(svg, spec)
        elif composition == "sequence":
            spec = sequence.load_spec(args.spec)
            svg = sequence.render(spec)
            sequence.validate_svg(svg, spec)
        else:
            raise sequence.SpecError(
                "set composition to 'explanatory' for a blog diagram, or 'sequence' "
                "when the post explains the order of an exchange."
            )
    except (sequence.SpecError, sequence.LayoutError, json.JSONDecodeError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(svg)
    print(f"wrote {args.output}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
