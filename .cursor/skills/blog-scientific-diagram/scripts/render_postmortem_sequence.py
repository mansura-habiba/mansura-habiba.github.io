#!/usr/bin/env python3
"""Render a publication incident post-mortem sequence diagram to SVG.

The canvas is fixed: 17.5 cm by 9.84375 cm (16:9), 10% margins, 96 dpi user
units so that a 2px stroke and 10pt/12pt type match the publication spec.
"""

from __future__ import annotations

import argparse
import json
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

ALLOWED_COLORS = {"#FFFFFF", "#000000", "#0066CC", "#F4B400", "#FF0000"}
FONT = "Arial, Helvetica, sans-serif"
PT_10 = 10 * 96 / 72  # 13.333...
PT_12 = 12 * 96 / 72  # 16
WIDTH_CM = 17.5
HEIGHT_CM = 17.5 * 9 / 16
MARGIN = 0.10
GATE_LABEL = "Missing Retrieval Gate"

NAMESPACES_SKIP = (
    "linearGradient",
    "radialGradient",
    "filter",
    "feDropShadow",
    "style",
    "script",
)


def px_from_cm(cm: float) -> float:
    return cm / 2.54 * 96


WIDTH = px_from_cm(WIDTH_CM)
HEIGHT = px_from_cm(HEIGHT_CM)


class SpecError(ValueError):
    pass


class LayoutError(ValueError):
    pass


def text_width(text: str, font_px: float, bold: bool) -> float:
    factor = 0.56 if bold else 0.52
    return len(text) * font_px * factor


def wrap_text(text: str, font_px: float, bold: bool, max_width: float) -> list[str]:
    words = text.split()
    if not words:
        raise SpecError("empty text is not allowed")
    lines: list[str] = []
    current = ""
    for word in words:
        trial = word if not current else f"{current} {word}"
        if text_width(trial, font_px, bold) <= max_width:
            current = trial
            continue
        if not current:
            raise LayoutError(f"label {word!r} is wider than {max_width:.0f}px at this type size")
        lines.append(current)
        current = word
    if current:
        lines.append(current)
    return lines


def require_keys(obj: dict, allowed: set[str], required: set[str], where: str) -> None:
    extra = set(obj) - allowed
    missing = required - set(obj)
    if extra:
        raise SpecError(f"{where} has unknown keys: {sorted(extra)}")
    if missing:
        raise SpecError(f"{where} is missing keys: {sorted(missing)}")


def load_spec(path: Path) -> dict:
    data = json.loads(path.read_text())
    if not isinstance(data, dict):
        raise SpecError("spec must be a JSON object")
    require_keys(
        data,
        {"title", "subfigure", "actors", "events", "incident", "composition"},
        {"title", "actors", "events"},
        "spec",
    )
    if data.get("composition") not in (None, "sequence"):
        raise SpecError("sequence specs must set composition to 'sequence'")
    if not isinstance(data["title"], str) or not data["title"].strip():
        raise SpecError("title must be a non-empty string")
    if "subfigure" in data and (
        not isinstance(data["subfigure"], str) or len(data["subfigure"]) != 1 or not data["subfigure"].isalpha()
    ):
        raise SpecError("subfigure must be a single letter")
    actors = data["actors"]
    if not isinstance(actors, list) or not 2 <= len(actors) <= 6:
        raise SpecError("actors must be a list of 2 to 6")
    ids: list[str] = []
    for i, actor in enumerate(actors):
        if not isinstance(actor, dict):
            raise SpecError(f"actors[{i}] must be an object")
        require_keys(actor, {"id", "name"}, {"id", "name"}, f"actors[{i}]")
        if not isinstance(actor["id"], str) or not actor["id"].isidentifier():
            raise SpecError(f"actors[{i}].id must be an identifier")
        if not isinstance(actor["name"], str) or not actor["name"].strip():
            raise SpecError(f"actors[{i}].name must be a non-empty string")
        ids.append(actor["id"])
    if len(set(ids)) != len(ids):
        raise SpecError("actor ids must be unique")
    events = data["events"]
    if not isinstance(events, list) or not events:
        raise SpecError("events must be a non-empty list")
    gates = 0
    for i, event in enumerate(events):
        if not isinstance(event, dict):
            raise SpecError(f"events[{i}] must be an object")
        kind = event.get("kind")
        if kind == "message":
            require_keys(
                event,
                {"kind", "from", "to", "label", "path", "time"},
                {"kind", "from", "to", "label", "path"},
                f"events[{i}]",
            )
            if event["from"] not in ids or event["to"] not in ids:
                raise SpecError(f"events[{i}] references an unknown actor")
            if event["path"] not in {"standard", "failure"}:
                raise SpecError(f"events[{i}].path must be 'standard' or 'failure'")
            if not isinstance(event["label"], str) or not event["label"].strip():
                raise SpecError(f"events[{i}].label must be a non-empty string")
        elif kind == "missing_retrieval_gate":
            require_keys(
                event,
                {"kind", "between", "time"},
                {"kind", "between"},
                f"events[{i}]",
            )
            between = event["between"]
            if (
                not isinstance(between, list)
                or len(between) != 2
                or between[0] not in ids
                or between[1] not in ids
                or between[0] == between[1]
            ):
                raise SpecError(f"events[{i}].between must be two distinct actor ids")
            gates += 1
        else:
            raise SpecError(f"events[{i}].kind must be 'message' or 'missing_retrieval_gate'")
        if "time" in event and (not isinstance(event["time"], str) or not event["time"].strip()):
            raise SpecError(f"events[{i}].time must be a non-empty string")
    if gates > 1:
        raise SpecError("at most one missing_retrieval_gate is allowed")
    if "incident" in data:
        incident = data["incident"]
        if not isinstance(incident, dict):
            raise SpecError("incident must be an object")
        require_keys(incident, {"label", "start", "end"}, {"label", "start", "end"}, "incident")
        if not isinstance(incident["label"], str) or not incident["label"].strip():
            raise SpecError("incident.label must be a non-empty string")
        start, end = incident["start"], incident["end"]
        if not isinstance(start, int) or not isinstance(end, int):
            raise SpecError("incident start and end must be integers")
        if not 0 <= start <= end < len(events):
            raise SpecError("incident span is outside the event list")
    return data


def esc(text: str) -> str:
    return (
        text.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace('"', "&quot;")
    )


def fmt(value: float) -> str:
    return f"{value:.2f}"


class Box:
    def __init__(self, x: float, y: float, w: float, h: float, what: str):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.what = what

    def inside(self, x0: float, y0: float, x1: float, y1: float) -> None:
        if self.x < x0 - 0.5 or self.y < y0 - 0.5 or self.x + self.w > x1 + 0.5 or self.y + self.h > y1 + 0.5:
            raise LayoutError(
                f"{self.what} falls outside the 10% margin "
                f"({self.x:.1f},{self.y:.1f},{self.w:.1f},{self.h:.1f})"
            )


def subtract_intervals(span: tuple[float, float], cuts: list[tuple[float, float]]) -> list[tuple[float, float]]:
    segments = [span]
    for cut_top, cut_bot in sorted(cuts):
        nxt: list[tuple[float, float]] = []
        for top, bot in segments:
            if cut_bot <= top or cut_top >= bot:
                nxt.append((top, bot))
                continue
            if cut_top > top:
                nxt.append((top, cut_top))
            if cut_bot < bot:
                nxt.append((cut_bot, bot))
        segments = nxt
    return [(top, bot) for top, bot in segments if bot - top > 2]


def render(spec: dict) -> str:
    x0, y0 = WIDTH * MARGIN, HEIGHT * MARGIN
    x1, y1 = WIDTH * (1 - MARGIN), HEIGHT * (1 - MARGIN)
    content_w, content_h = x1 - x0, y1 - y0
    boxes: list[Box] = []

    def track(x: float, y: float, w: float, h: float, what: str) -> None:
        box = Box(x, y, w, h, what)
        box.inside(x0, y0, x1, y1)
        boxes.append(box)

    title_baseline = y0 + PT_12
    track(
        x0,
        title_baseline - PT_12 * 0.82,
        content_w,
        PT_12,
        "title line",
    )
    title_w = text_width(spec["title"], PT_12, True)
    if title_w > content_w - (48 if "subfigure" in spec else 8):
        raise LayoutError("title does not fit the content width at 12pt")

    has_time = any("time" in event for event in spec["events"])
    gutter = 52.0 if has_time else 8.0
    n = len(spec["actors"])
    usable = content_w - gutter
    pitch = usable / n
    centers = [x0 + gutter + pitch * (i + 0.5) for i in range(n)]
    id_to_x = {actor["id"]: centers[i] for i, actor in enumerate(spec["actors"])}

    max_name_w = pitch - 18
    actor_layouts = []
    line_h = PT_10 * 1.25
    for actor in spec["actors"]:
        lines = wrap_text(actor["name"], PT_10, True, max_name_w)
        block_w = max(text_width(line, PT_10, True) for line in lines) + 16
        block_h = line_h * len(lines) + 12
        actor_layouts.append((lines, block_w, block_h))
    actor_h = max(block_h for _, _, block_h in actor_layouts)
    actor_top = title_baseline + 14
    if actor_top + actor_h > y1:
        raise LayoutError("actor row does not fit under the title")

    actor_bottom = actor_top + actor_h
    life_top = actor_bottom
    life_bottom = y1 - 6
    event_top = life_top + 22
    event_bottom = life_bottom - 8
    count = len(spec["events"])
    if count == 1:
        event_ys = [(event_top + event_bottom) / 2]
        row_gap = 36.0
    else:
        span = event_bottom - event_top
        row_gap = span / (count - 1)
        if row_gap < 34:
            raise LayoutError(
                f"{count} events do not fit this 16:9 panel (row gap {row_gap:.0f}px). "
                "Split the timeline into subfigures."
            )
        event_ys = [event_top + i * row_gap for i in range(count)]

    back: list[str] = [
        f'<rect x="0" y="0" width="{fmt(WIDTH)}" height="{fmt(HEIGHT)}" fill="#FFFFFF"/>'
    ]
    front: list[str] = []
    # Vertical spans where a lifeline would strike text or the risk box.
    cuts: dict[float, list[tuple[float, float]]] = {cx: [] for cx in centers}

    def cut_lifelines(text_x: float, text_w: float, top: float, height: float) -> None:
        pad = 3.0
        for cx in centers:
            if text_x - pad <= cx <= text_x + text_w + pad:
                cuts[cx].append((top - pad, top + height + pad))

    band_top = band_bot = None
    if "incident" in spec:
        start, end = spec["incident"]["start"], spec["incident"]["end"]
        band_top = event_ys[start] - row_gap * 0.48
        band_bot = event_ys[end] + row_gap * 0.48
        band_top = max(band_top, life_top + 4)
        band_bot = min(band_bot, life_bottom)
        band_h = band_bot - band_top
        track(x0, band_top, content_w, band_h, "incident highlight")
        back.append(
            f'<rect id="incident-highlight" x="{fmt(x0)}" y="{fmt(band_top)}" '
            f'width="{fmt(content_w)}" height="{fmt(band_h)}" rx="4" ry="4" '
            f'fill="#F4B400" stroke="#000000" stroke-width="2"/>'
        )
        label = spec["incident"]["label"]
        label_w = text_width(label, PT_10, False)
        # Sit the label just above the band so it does not share a cell with a timestamp.
        label_x = x0
        label_y = band_top - 4
        label_top = label_y - PT_10 * 0.82
        if label_top < actor_bottom + 4:
            label_x = x1 - label_w
            label_y = band_top + PT_10 + 4
            label_top = label_y - PT_10 * 0.82
        track(label_x, label_top, label_w, PT_10, "incident label")
        cut_lifelines(label_x, label_w, label_top, PT_10)
        front.append(
            f'<text id="incident-label" x="{fmt(label_x)}" y="{fmt(label_y)}" '
            f'fill="#000000" font-family="{FONT}" font-size="{PT_10:.3f}" '
            f'font-weight="400">{esc(label)}</text>'
        )

    for index, event in enumerate(spec["events"]):
        y = event_ys[index]
        if "time" in event:
            tw = text_width(event["time"], PT_10, False)
            tx = x0 + gutter - 10 - tw
            track(tx, y - PT_10 * 0.75, tw, PT_10, f"time {event['time']}")
            front.append(
                f'<text x="{fmt(tx)}" y="{fmt(y + 4)}" fill="#000000" '
                f'font-family="{FONT}" font-size="{PT_10:.3f}" font-weight="400">'
                f'{esc(event["time"])}</text>'
            )
        if event["kind"] == "message":
            color = "#000000" if event["path"] == "standard" else "#0066CC"
            marker = "arrow-standard" if event["path"] == "standard" else "arrow-failure"
            x_from = id_to_x[event["from"]]
            x_to = id_to_x[event["to"]]
            if event["from"] == event["to"]:
                reach = 28.0
                d = f'M {fmt(x_from)} {fmt(y)} h {fmt(reach)} v 16 h {fmt(-reach)}'
                front.append(
                    f'<path d="{d}" fill="none" stroke="{color}" stroke-width="1.5" '
                    f'marker-end="url(#{marker})"/>'
                )
                lx = x_from + reach + 6
                lw = text_width(event["label"], PT_10, False)
                label_top = y - 2
                track(lx, label_top, lw, PT_10, event["label"])
                cut_lifelines(lx, lw, label_top, PT_10)
                front.append(
                    f'<text class="interaction" x="{fmt(lx)}" y="{fmt(y + 8)}" fill="#000000" '
                    f'font-family="{FONT}" font-size="{PT_10:.3f}" font-weight="400">'
                    f'{esc(event["label"])}</text>'
                )
            else:
                front.append(
                    f'<line class="interaction" data-path="{event["path"]}" '
                    f'x1="{fmt(x_from)}" y1="{fmt(y)}" x2="{fmt(x_to)}" y2="{fmt(y)}" '
                    f'stroke="{color}" stroke-width="1.5" marker-end="url(#{marker})"/>'
                )
                mid = (x_from + x_to) / 2
                lw = text_width(event["label"], PT_10, False)
                label_top = y - 6 - PT_10 * 0.82
                track(mid - lw / 2, label_top, lw, PT_10, event["label"])
                cut_lifelines(mid - lw / 2, lw, label_top, PT_10)
                front.append(
                    f'<text class="interaction" x="{fmt(mid)}" y="{fmt(y - 6)}" '
                    f'text-anchor="middle" fill="#000000" font-family="{FONT}" '
                    f'font-size="{PT_10:.3f}" font-weight="400">{esc(event["label"])}</text>'
                )
        else:
            a, b = event["between"]
            left, right = sorted((id_to_x[a], id_to_x[b]))
            gap = right - left
            box_w = min(gap - 20, max(text_width(GATE_LABEL, PT_10, False) + 16, 120))
            lines = wrap_text(GATE_LABEL, PT_10, False, box_w - 12)
            box_h = line_h * len(lines) + 12
            box_w = max(text_width(line, PT_10, False) for line in lines) + 16
            if box_w > gap - 8:
                raise LayoutError("Missing Retrieval Gate box does not fit between its lifelines")
            bx = (left + right) / 2 - box_w / 2
            by = y - box_h / 2
            track(bx, by, box_w, box_h, GATE_LABEL)
            cut_lifelines(bx, box_w, by, box_h)
            front.append(
                f'<rect id="missing-retrieval-gate" x="{fmt(bx)}" y="{fmt(by)}" '
                f'width="{fmt(box_w)}" height="{fmt(box_h)}" rx="4" ry="4" '
                f'fill="#FF0000" stroke="#000000" stroke-width="2"/>'
            )
            text_y = by + 6 + PT_10 * 0.82
            tspans = []
            for line_i, line in enumerate(lines):
                if line_i == 0:
                    tspans.append(f'<tspan x="{fmt(bx + box_w / 2)}" y="{fmt(text_y)}">{esc(line)}</tspan>')
                else:
                    tspans.append(
                        f'<tspan x="{fmt(bx + box_w / 2)}" dy="{fmt(line_h)}">{esc(line)}</tspan>'
                    )
            front.append(
                f'<text id="missing-retrieval-gate-label" text-anchor="middle" fill="#000000" '
                f'font-family="{FONT}" font-size="{PT_10:.3f}" font-weight="400">'
                + "".join(tspans)
                + "</text>"
            )

    for (lines, block_w, _), cx in zip(actor_layouts, centers):
        bx = cx - block_w / 2
        track(bx, actor_top, block_w, actor_h, "actor")
        front.append(
            f'<rect class="actor" x="{fmt(bx)}" y="{fmt(actor_top)}" width="{fmt(block_w)}" '
            f'height="{fmt(actor_h)}" rx="4" ry="4" fill="#FFFFFF" stroke="#000000" stroke-width="2"/>'
        )
        text_y = actor_top + (actor_h - line_h * len(lines)) / 2 + PT_10 * 0.82
        tspans = []
        for line_i, line in enumerate(lines):
            if line_i == 0:
                tspans.append(f'<tspan x="{fmt(cx)}" y="{fmt(text_y)}">{esc(line)}</tspan>')
            else:
                tspans.append(f'<tspan x="{fmt(cx)}" dy="{fmt(line_h)}">{esc(line)}</tspan>')
        front.append(
            f'<text class="actor-name" text-anchor="middle" fill="#000000" font-family="{FONT}" '
            f'font-size="{PT_10:.3f}" font-weight="700">' + "".join(tspans) + "</text>"
        )

    if "subfigure" in spec:
        sub = f"({spec['subfigure']})"
        sub_w = text_width(sub, PT_12, True)
        track(x0, title_baseline - PT_12 * 0.82, sub_w, PT_12, "subfigure")
        front.append(
            f'<text id="subfigure" x="{fmt(x0)}" y="{fmt(title_baseline)}" fill="#000000" '
            f'font-family="{FONT}" font-size="{PT_12:.3f}" font-weight="700">{esc(sub)}</text>'
        )

    lifelines: list[str] = []
    for cx in centers:
        for top, bot in subtract_intervals((life_top, life_bottom), cuts[cx]):
            lifelines.append(
                f'<line x1="{fmt(cx)}" y1="{fmt(top)}" x2="{fmt(cx)}" y2="{fmt(bot)}" '
                f'stroke="#000000" stroke-width="1" stroke-dasharray="4 3"/>'
            )
    parts = back + lifelines + front

    title_x = (x0 + x1) / 2
    parts.append(
        f'<text id="figure-title" x="{fmt(title_x)}" y="{fmt(title_baseline)}" text-anchor="middle" '
        f'fill="#000000" font-family="{FONT}" font-size="{PT_12:.3f}" font-weight="700">'
        f'{esc(spec["title"])}</text>'
    )

    marker_bits = [
        '<marker id="arrow-standard" markerUnits="userSpaceOnUse" markerWidth="10" markerHeight="8" refX="9" refY="4" orient="auto">',
        '<path d="M0,0 L10,4 L0,8 Z" fill="#000000"/>',
        "</marker>",
    ]
    if any(event.get("path") == "failure" for event in spec["events"]):
        marker_bits.extend(
            [
                '<marker id="arrow-failure" markerUnits="userSpaceOnUse" markerWidth="10" markerHeight="8" refX="9" refY="4" orient="auto">',
                '<path d="M0,0 L10,4 L0,8 Z" fill="#0066CC"/>',
                "</marker>",
            ]
        )
    markers = "  <defs>\n    " + "\n    ".join(marker_bits) + "\n  </defs>"
    body = "\n  ".join(parts)
    return (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{WIDTH_CM}cm" height="{HEIGHT_CM:.5f}cm" '
        f'viewBox="0 0 {WIDTH:.3f} {HEIGHT:.3f}" role="img">\n'
        f"  <title>{esc(spec['title'])}</title>\n"
        f"{markers}\n"
        f"  {body}\n"
        "</svg>\n"
    )


def figure_flags(spec: dict) -> tuple[bool, bool, bool]:
    """Gate, failure-path, and incident flags for either composition."""
    if "rows" in spec:
        layers = [layer for row in spec["rows"] for layer in row["layers"]]
        gate = any(layer.get("role") == "risk" for layer in layers)
        failure = any(layer.get("role") == "failure" for layer in layers)
        incident = any(layer.get("role") == "incident" for layer in layers)
        return gate, failure, incident
    events = spec["events"]
    gate = any(event["kind"] == "missing_retrieval_gate" for event in events)
    failure = any(event.get("path") == "failure" for event in events)
    return gate, failure, "incident" in spec


def local(tag: str) -> str:
    return tag.rsplit("}", 1)[-1]


def validate_svg(svg: str, spec: dict) -> None:
    root = ET.fromstring(svg)
    if local(root.tag) != "svg":
        raise SpecError("root element must be svg")
    if root.get("width") != f"{WIDTH_CM}cm":
        raise SpecError(f"width must be {WIDTH_CM}cm")
    height_cm = float(root.get("height", "0cm")[:-2])
    view = root.get("viewBox", "").split()
    if len(view) != 4 or abs(float(view[2]) - WIDTH) > 0.01:
        raise SpecError("viewBox width does not match the 17.5cm canvas")
    if "rows" in spec:
        if height_cm + 1e-3 < HEIGHT_CM:
            raise SpecError("explanatory figure must be at least 16:9")
        expected_h = height_cm / 2.54 * 96
        if abs(float(view[3]) - expected_h) > 0.05:
            raise SpecError("viewBox height does not match the stated height")
    else:
        if abs(height_cm - HEIGHT_CM) > 1e-4:
            raise SpecError("height must be 17.5cm × 9/16")
        if abs(float(view[3]) - HEIGHT) > 0.01:
            raise SpecError("viewBox does not match the 96 dpi canvas")

    red_ids = []
    yellow_ids = []
    blue_nodes = 0
    rounded = 0
    fonts = set()
    for elem in root.iter():
        name = local(elem.tag)
        if name in NAMESPACES_SKIP or name.startswith("fe"):
            raise SpecError(f"forbidden element <{name}>")
        style = elem.get("style")
        if style:
            raise SpecError("style attributes are not allowed")
        if elem.get("opacity") not in (None, "1"):
            raise SpecError("opacity is not allowed")
        if elem.get("filter") or elem.get("clip-path"):
            raise SpecError("filters and clips are not allowed")
        for attr in ("fill", "stroke"):
            value = elem.get(attr)
            if value in (None, "none"):
                continue
            if value not in ALLOWED_COLORS:
                raise SpecError(f"color {value} is outside the palette")
            if value == "#FF0000":
                red_ids.append(elem.get("id"))
            if value == "#F4B400":
                yellow_ids.append(elem.get("id"))
            if value == "#0066CC":
                blue_nodes += 1
        if elem.get("font-family"):
            fonts.add(elem.get("font-family"))
        if name == "rect" and elem.get("stroke-width") not in (None, "2"):
            raise SpecError("every stroked rectangle uses a 2px border")
        if name == "rect" and elem.get("rx"):
            rounded += 1
            if elem.get("stroke") != "#000000" or elem.get("stroke-width") != "2":
                raise SpecError("rounded rectangles need a 2px black border")

    if fonts != {FONT}:
        raise SpecError(f"font-family must be {FONT}")
    title = root.find(".//*[@id='figure-title']")
    if title is None or abs(float(title.get("font-size")) - PT_12) > 0.01 or title.get("font-weight") != "700":
        raise SpecError("figure title must be 12pt bold")
    if "subfigure" in spec:
        sub = root.find(".//*[@id='subfigure']")
        if sub is None or sub.get("font-weight") != "700" or sub.text != f"({spec['subfigure']})":
            raise SpecError("subfigure label must be 12pt bold")
    for text in root.iter():
        if local(text.tag) == "text" and "interaction" in (text.get("class") or "").split():
            if abs(float(text.get("font-size")) - PT_10) > 0.01 or text.get("font-weight") != "400":
                raise SpecError("interaction labels must be 10pt regular")
            if text.get("fill") != "#000000":
                raise SpecError("interaction labels must be black")
    for text in root.iter():
        if local(text.tag) == "text" and "actor-name" in (text.get("class") or "").split():
            if text.get("font-weight") != "700":
                raise SpecError("actor names must be bold")

    expects_gate, expects_failure, expects_incident = figure_flags(spec)
    if expects_gate:
        if red_ids != ["missing-retrieval-gate"]:
            raise SpecError("red is permitted only on the Missing Retrieval Gate rectangle")
    elif red_ids:
        raise SpecError("red appeared without a Missing Retrieval Gate")
    if expects_incident:
        if yellow_ids != ["incident-highlight"]:
            raise SpecError("yellow is permitted only on the incident highlight")
    elif yellow_ids:
        raise SpecError("yellow appeared without an incident span")
    if expects_failure and blue_nodes < 1:
        raise SpecError("failure path is missing its blue stroke")
    if not expects_failure and blue_nodes:
        raise SpecError("blue appeared without a failure path")
    for marker in root.iter():
        if local(marker.tag) != "marker":
            continue
        path = next(child for child in marker if local(child.tag) == "path")
        if "Z" not in path.get("d", "") or path.get("fill") not in {"#000000", "#0066CC"}:
            raise SpecError("arrowheads must be solid triangles")
    if rounded < 1:
        raise SpecError("expected rounded rectangles")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("spec", type=Path)
    parser.add_argument("-o", "--output", type=Path, required=True)
    args = parser.parse_args(argv)
    try:
        spec = load_spec(args.spec)
        svg = render(spec)
        validate_svg(svg, spec)
    except (SpecError, LayoutError, json.JSONDecodeError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(svg)
    print(f"wrote {args.output}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
