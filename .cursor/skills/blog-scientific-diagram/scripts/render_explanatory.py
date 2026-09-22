#!/usr/bin/env python3
"""Layered scientific diagram for a blog post.

Bands, chips, a downward flow, and an optional return path. Flat fills only.
"""

from __future__ import annotations

import sys
import xml.etree.ElementTree as ET
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import render_postmortem_sequence as canvas

SpecError = canvas.SpecError
LayoutError = canvas.LayoutError
FONT = canvas.FONT
PT_10 = canvas.PT_10
PT_12 = canvas.PT_12
PT_CHIP = 8.5 * 96 / 72
ARROW = "#1E3A5F"
INK = "#1A1A1A"

TONES = {
    "blue": {"fill": "#E8F1FC", "accent": "#2B6CB0"},
    "green": {"fill": "#E7F6EC", "accent": "#2F7D4A"},
    "purple": {"fill": "#F3EAF8", "accent": "#6B3FA0"},
    "teal": {"fill": "#E5F6F5", "accent": "#1A7A78"},
    "amber": {"fill": "#FFF6E8", "accent": "#C47B16"},
    "orange": {"fill": "#FFF1E8", "accent": "#D35400"},
}

ALLOWED = {ARROW, INK, "#FFFFFF", "#000000"}
for tone in TONES.values():
    ALLOWED.update(tone.values())


def load_spec(data: dict) -> dict:
    canvas.require_keys(
        data,
        {"composition", "title", "layers", "return"},
        {"composition", "title", "layers"},
        "spec",
    )
    if data["composition"] != "explanatory":
        raise SpecError("explanatory specs must set composition to 'explanatory'")
    if not isinstance(data["title"], str) or not data["title"].strip():
        raise SpecError("title must be a non-empty string")
    layers = data["layers"]
    if not isinstance(layers, list) or not 2 <= len(layers) <= 8:
        raise SpecError("layers must be a list of 2 to 8")
    ids: list[str] = []
    for i, layer in enumerate(layers):
        if not isinstance(layer, dict):
            raise SpecError(f"layers[{i}] must be an object")
        kind = layer.get("kind")
        if kind == "band":
            _band(layer, f"layers[{i}]")
            ids.append(layer["id"])
        elif kind == "flow":
            _flow(layer, f"layers[{i}]")
            ids.append(layer["id"])
        elif kind == "split":
            columns = layer.get("columns")
            if not isinstance(columns, list) or len(columns) != 2:
                raise SpecError(f"layers[{i}].columns must contain two bands")
            for j, column in enumerate(columns):
                _band(column, f"layers[{i}].columns[{j}]")
                ids.append(column["id"])
        else:
            raise SpecError(f"layers[{i}].kind must be 'band', 'flow', or 'split'")
    if len(set(ids)) != len(ids):
        raise SpecError("layer ids must be unique")
    if "return" in data:
        link = data["return"]
        if not isinstance(link, dict):
            raise SpecError("return must be an object")
        canvas.require_keys(link, {"from", "to"}, {"from", "to"}, "return")
        if link["from"] not in ids or link["to"] not in ids:
            raise SpecError("return endpoints must be layer ids")
    return data


def _band(layer: dict, where: str) -> None:
    canvas.require_keys(
        layer,
        {"kind", "id", "title", "tone", "icon", "chips"},
        {"id", "title", "tone", "chips"},
        where,
    )
    if not isinstance(layer["id"], str) or not layer["id"].isidentifier():
        raise SpecError(f"{where}.id must be an identifier")
    if not isinstance(layer["title"], str) or not layer["title"].strip():
        raise SpecError(f"{where}.title must be a non-empty string")
    if layer["tone"] not in TONES:
        raise SpecError(f"{where}.tone must be one of {sorted(TONES)}")
    chips = layer["chips"]
    if not isinstance(chips, list) or not chips or any(not isinstance(c, str) or not c.strip() for c in chips):
        raise SpecError(f"{where}.chips must be a non-empty list of labels")
    if "icon" in layer and layer["icon"] not in {
        "shield",
        "key",
        "chip",
        "database",
        "sliders",
        "clipboard",
        "search",
    }:
        raise SpecError(f"{where}.icon is not a known icon")


def _flow(layer: dict, where: str) -> None:
    canvas.require_keys(
        layer,
        {"kind", "id", "title", "tone", "icon", "source", "lanes", "sink"},
        {"kind", "id", "title", "tone", "source", "lanes", "sink"},
        where,
    )
    if layer["tone"] not in TONES:
        raise SpecError(f"{where}.tone must be one of {sorted(TONES)}")
    if not isinstance(layer["id"], str) or not layer["id"].isidentifier():
        raise SpecError(f"{where}.id must be an identifier")
    lanes = layer["lanes"]
    if not isinstance(lanes, list) or not 2 <= len(lanes) <= 4:
        raise SpecError(f"{where}.lanes must contain 2 to 4 rows")
    for j, lane in enumerate(lanes):
        if not isinstance(lane, list) or len(lane) != 2 or any(not isinstance(x, str) or not x.strip() for x in lane):
            raise SpecError(f"{where}.lanes[{j}] must be two labels")
    for key in ("title", "source", "sink"):
        if not isinstance(layer[key], str) or not layer[key].strip():
            raise SpecError(f"{where}.{key} must be a non-empty string")


def _icon(name: str, x: float, y: float, color: str) -> str:
    common = (
        f'fill="none" stroke="{color}" stroke-width="1.7" '
        'stroke-linejoin="round" stroke-linecap="round"'
    )
    bodies = {
        "shield": f'<path {common} d="M13 2.5 L22 6.2 V12.5 C22 17.2 18 21 13 22.5 C8 21 4 17.2 4 12.5 V6.2 Z"/>',
        "key": (
            f'<circle {common} cx="8" cy="13" r="3.2"/>'
            f'<path {common} d="M11 13 H21 M18 13 V16 M21 13 V15.5"/>'
        ),
        "chip": (
            f'<rect {common} x="7" y="7" width="12" height="12" rx="2"/>'
            f'<path {common} d="M10 7 V4 M16 7 V4 M10 19 V22 M16 19 V22 M7 10 H4 M7 16 H4 M19 10 H22 M19 16 H22"/>'
        ),
        "database": (
            f'<ellipse {common} cx="13" cy="7" rx="7" ry="3"/>'
            f'<path {common} d="M6 7 V17 C6 18.7 9.1 20 13 20 C16.9 20 20 18.7 20 17 V7"/>'
            f'<path {common} d="M6 12 C6 13.7 9.1 15 13 15 C16.9 15 20 13.7 20 12"/>'
        ),
        "sliders": (
            f'<path {common} d="M5 8 H21 M5 13 H21 M5 18 H21"/>'
            f'<circle {common} cx="10" cy="8" r="2"/><circle {common} cx="16" cy="13" r="2"/>'
            f'<circle {common} cx="12" cy="18" r="2"/>'
        ),
        "clipboard": (
            f'<rect {common} x="6" y="5" width="14" height="17" rx="2"/>'
            f'<path {common} d="M10 5 V4 H16 V5 M9 12 L12 15 L17 9"/>'
        ),
        "search": (
            f'<circle {common} cx="11" cy="11" r="5.5"/>'
            f'<path {common} d="M15.2 15.2 L21 21"/>'
        ),
    }
    if name not in bodies:
        name = "shield"
    return f'<g transform="translate({canvas.fmt(x)} {canvas.fmt(y)})">{bodies[name]}</g>'


def _chip_width(label: str, font_px: float) -> float:
    return len(label) * font_px * 0.47 + 12


def _chips(labels: list[str], cx: float, y: float, max_w: float, accent: str) -> tuple[str, float]:
    gap = 6.0
    height = 20.0
    font_px = PT_CHIP
    widths = [_chip_width(label, font_px) for label in labels]
    while sum(widths) + gap * (len(labels) - 1) > max_w and font_px > 9.5:
        font_px -= 0.5
        widths = [_chip_width(label, font_px) for label in labels]
    total = sum(widths) + gap * (len(labels) - 1)
    if total > max_w:
        raise LayoutError("chips do not fit the band; shorten the labels")
    x = cx - total / 2
    parts = []
    for label, width in zip(labels, widths):
        parts.append(
            f'<rect x="{canvas.fmt(x)}" y="{canvas.fmt(y)}" width="{canvas.fmt(width)}" '
            f'height="{height}" rx="8" fill="#FFFFFF" stroke="{accent}" stroke-width="1.4"/>'
        )
        parts.append(
            f'<text x="{canvas.fmt(x + width / 2)}" y="{canvas.fmt(y + 14)}" text-anchor="middle" '
            f'fill="{INK}" font-family="{FONT}" font-size="{font_px:.3f}" font-weight="400">'
            f"{canvas.esc(label)}</text>"
        )
        x += width + gap
    return "\n  ".join(parts), height


def _rounded(x, y, w, h, fill, stroke, rx=12, sw="2", extra="") -> str:
    return (
        f'<rect {extra} x="{canvas.fmt(x)}" y="{canvas.fmt(y)}" width="{canvas.fmt(w)}" '
        f'height="{canvas.fmt(h)}" rx="{rx}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>'
    )


def _title(text, x, y, color, size, weight, anchor="middle") -> str:
    return (
        f'<text x="{canvas.fmt(x)}" y="{canvas.fmt(y)}" text-anchor="{anchor}" fill="{color}" '
        f'font-family="{FONT}" font-size="{size:.3f}" font-weight="{weight}">{canvas.esc(text)}</text>'
    )


def _varrow(x: float, y1: float, y2: float) -> str:
    return (
        f'<line x1="{canvas.fmt(x)}" y1="{canvas.fmt(y1)}" x2="{canvas.fmt(x)}" y2="{canvas.fmt(y2)}" '
        f'stroke="{ARROW}" stroke-width="1.6" marker-end="url(#arrow-down)"/>'
    )


def render(spec: dict) -> str:
    margin = canvas.WIDTH * 0.10
    inner_w = canvas.WIDTH - 2 * margin
    has_return = "return" in spec
    rail_gap = 30.0 if has_return else 0.0
    band_w = inner_w - rail_gap
    band_x = margin
    title_baseline = margin + PT_12
    cursor = title_baseline + 16
    gap = 26.0
    simple_h = 78.0
    flow_h = 128.0
    placed = []
    id_box: dict[str, tuple[float, float, float, float]] = {}

    for index, layer in enumerate(spec["layers"]):
        if index:
            cursor += gap
        kind = layer["kind"]
        height = flow_h if kind == "flow" else simple_h
        placed.append((cursor, height, layer))
        if kind == "split":
            col_gap = 18.0
            col_w = (band_w - col_gap) / 2
            id_box[layer["columns"][0]["id"]] = (band_x, cursor, col_w, height)
            id_box[layer["columns"][1]["id"]] = (band_x + col_w + col_gap, cursor, col_w, height)
        else:
            id_box[layer["id"]] = (band_x, cursor, band_w, height)
        cursor += height

    total_h = cursor + margin
    parts: list[str] = [
        f'<rect x="0" y="0" width="{canvas.fmt(canvas.WIDTH)}" height="{canvas.fmt(total_h)}" fill="#FFFFFF"/>',
        _title(spec["title"], canvas.WIDTH / 2, title_baseline, INK, PT_12, "700"),
    ]

    def paint_band(x, y, w, h, layer) -> None:
        tone = TONES[layer["tone"]]
        icon = layer.get("icon", "shield")
        parts.append(_rounded(x, y, w, h, tone["fill"], tone["accent"]))
        parts.append(_icon(icon, x + 12, y + h / 2 - 13, tone["accent"]))
        parts.append(_title(layer["title"], x + w / 2, y + 28, tone["accent"], PT_10 + 1, "700"))
        chip_markup, _ = _chips(layer["chips"], x + w / 2, y + 40, w - 16, tone["accent"])
        parts.append(chip_markup)

    for index, (y, height, layer) in enumerate(placed):
        if layer["kind"] == "band":
            paint_band(band_x, y, band_w, height, layer)
        elif layer["kind"] == "split":
            for column_id in (layer["columns"][0]["id"], layer["columns"][1]["id"]):
                x, yy, w, h = id_box[column_id]
                column = next(col for col in layer["columns"] if col["id"] == column_id)
                paint_band(x, yy, w, h, column)
        else:
            tone = TONES[layer["tone"]]
            parts.append(_rounded(band_x, y, band_w, height, tone["fill"], tone["accent"]))
            parts.append(_icon(layer.get("icon", "chip"), band_x + 14, y + 18, tone["accent"]))
            parts.append(
                _title(layer["title"], band_x + 46, y + 68, tone["accent"], PT_10, "700", anchor="middle")
            )
            _paint_flow(parts, band_x, y, band_w, height, layer, tone["accent"])
        if index < len(placed) - 1:
            next_layer = placed[index + 1][2]
            y2 = y + height
            y3 = placed[index + 1][0]
            if layer["kind"] == "split":
                for column in layer["columns"]:
                    x, _, w, _ = id_box[column["id"]]
                    parts.append(_varrow(x + w / 2, y2 + 3, y3 - 5))
            elif next_layer["kind"] == "split":
                parts.append(_varrow(band_x + band_w / 2, y2 + 3, y3 - 5))
            else:
                parts.append(_varrow(band_x + band_w / 2, y2 + 3, y3 - 5))

    if has_return:
        src = id_box[spec["return"]["from"]]
        dst = id_box[spec["return"]["to"]]
        rail = band_x + band_w + 16
        y_from = src[1] + src[3] / 2
        y_to = dst[1] + dst[3] / 2
        x_from = src[0] + src[2]
        x_to = dst[0] + dst[2]
        radius = 10
        path = (
            f"M {canvas.fmt(x_from)} {canvas.fmt(y_from)} "
            f"H {canvas.fmt(rail - radius)} "
            f"Q {canvas.fmt(rail)} {canvas.fmt(y_from)} {canvas.fmt(rail)} {canvas.fmt(y_from - radius)} "
            f"V {canvas.fmt(y_to + radius)} "
            f"Q {canvas.fmt(rail)} {canvas.fmt(y_to)} {canvas.fmt(rail - radius)} {canvas.fmt(y_to)} "
            f"H {canvas.fmt(x_to)}"
        )
        parts.append(
            f'<path d="{path}" fill="none" stroke="{ARROW}" stroke-width="1.6" '
            f'marker-end="url(#arrow-return)"/>'
        )

    height_cm = total_h / canvas.WIDTH * canvas.WIDTH_CM
    markers = f"""  <defs>
    <marker id="arrow-down" markerUnits="userSpaceOnUse" markerWidth="10" markerHeight="8" refX="9" refY="4" orient="auto">
      <path d="M0,0 L10,4 L0,8 Z" fill="{ARROW}"/>
    </marker>
    <marker id="arrow-return" markerUnits="userSpaceOnUse" markerWidth="10" markerHeight="8" refX="9" refY="4" orient="auto">
      <path d="M0,0 L10,4 L0,8 Z" fill="{ARROW}"/>
    </marker>
    <marker id="arrow-flow" markerUnits="userSpaceOnUse" markerWidth="8" markerHeight="7" refX="7" refY="3.5" orient="auto">
      <path d="M0,0 L8,3.5 L0,7 Z" fill="{ARROW}"/>
    </marker>
  </defs>"""
    body = "\n  ".join(parts)
    return (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{canvas.WIDTH_CM}cm" height="{height_cm:.5f}cm" '
        f'viewBox="0 0 {canvas.WIDTH:.3f} {total_h:.3f}" role="img">\n'
        f"  <title>{canvas.esc(spec['title'])}</title>\n"
        f"{markers}\n"
        f"  {body}\n"
        "</svg>\n"
    )


def _paint_flow(parts: list[str], x: float, y: float, w: float, h: float, layer: dict, accent: str) -> None:
    pad = 8.0
    left = 78.0
    source_w = 72.0
    sink_w = 78.0
    arrow = 12.0
    lanes = layer["lanes"]
    inner = w - pad * 2 - left - source_w - sink_w - arrow * 4
    box_w = (inner - arrow) / 2
    if box_w < 70:
        raise LayoutError("execution lanes do not fit the figure width")
    lane_h = (h - pad * 2) / len(lanes)
    box_h = min(28.0, lane_h - 6)
    source_x = x + pad + left
    source_y = y + pad
    source_h = h - pad * 2
    sink_x = x + w - pad - sink_w
    parts.append(_rounded(source_x, source_y, source_w, source_h, "#FFFFFF", accent, rx=8))
    parts.append(
        _title(layer["source"], source_x + source_w / 2, source_y + source_h / 2 + 4, accent, PT_CHIP, "700")
    )
    parts.append(_rounded(sink_x, source_y, sink_w, source_h, "#FFFFFF", accent, rx=8))
    parts.append(
        _title(layer["sink"], sink_x + sink_w / 2, source_y + source_h / 2 + 4, accent, PT_CHIP, "700")
    )
    lane_x = source_x + source_w + arrow
    for i, (left_label, right_label) in enumerate(lanes):
        cy = y + pad + lane_h * i + lane_h / 2
        by = cy - box_h / 2
        parts.append(
            f'<line x1="{canvas.fmt(source_x + source_w)}" y1="{canvas.fmt(cy)}" '
            f'x2="{canvas.fmt(lane_x)}" y2="{canvas.fmt(cy)}" stroke="{accent}" stroke-width="1.3" '
            f'marker-end="url(#arrow-flow)"/>'
        )
        parts.append(_rounded(lane_x, by, box_w, box_h, "#FFFFFF", accent, rx=7, sw="1.4"))
        parts.append(_title(left_label, lane_x + box_w / 2, cy + 3.5, INK, PT_CHIP, "400"))
        mid_x = lane_x + box_w
        parts.append(
            f'<line x1="{canvas.fmt(mid_x)}" y1="{canvas.fmt(cy)}" '
            f'x2="{canvas.fmt(mid_x + arrow)}" y2="{canvas.fmt(cy)}" stroke="{accent}" stroke-width="1.3" '
            f'marker-end="url(#arrow-flow)"/>'
        )
        rx = mid_x + arrow
        parts.append(_rounded(rx, by, box_w, box_h, "#FFFFFF", accent, rx=7, sw="1.4"))
        parts.append(_title(right_label, rx + box_w / 2, cy + 3.5, INK, PT_CHIP, "400"))
        parts.append(
            f'<line x1="{canvas.fmt(rx + box_w)}" y1="{canvas.fmt(cy)}" '
            f'x2="{canvas.fmt(sink_x)}" y2="{canvas.fmt(cy)}" stroke="{accent}" stroke-width="1.3" '
            f'marker-end="url(#arrow-flow)"/>'
        )


def validate_svg(svg: str, spec: dict) -> None:
    root = ET.fromstring(svg)
    if root.get("width") != f"{canvas.WIDTH_CM}cm":
        raise SpecError("width must be 17.5cm")
    view = root.get("viewBox", "").split()
    if len(view) != 4 or abs(float(view[2]) - canvas.WIDTH) > 0.01:
        raise SpecError("viewBox width does not match 17.5cm at 96 dpi")
    title = root.find(".//*[@id='figure-title']") if False else None
    # Title is the first bold 12pt text; identify by font-size.
    fonts = set()
    for elem in root.iter():
        name = elem.tag.rsplit("}", 1)[-1]
        if name in {"linearGradient", "radialGradient", "filter", "style", "script"} or name.startswith("fe"):
            raise SpecError(f"forbidden element <{name}>")
        if elem.get("style") or elem.get("opacity") not in (None, "1") or elem.get("filter"):
            raise SpecError("gradients, shadows, and opacity are not allowed")
        for attr in ("fill", "stroke"):
            value = elem.get(attr)
            if value in (None, "none"):
                continue
            if value not in ALLOWED:
                raise SpecError(f"color {value} is outside the blog diagram palette")
        if elem.get("font-family"):
            fonts.add(elem.get("font-family"))
    if fonts != {FONT}:
        raise SpecError("font must be Arial, Helvetica, sans-serif")
    found_title = False
    for elem in root.iter():
        if elem.tag.rsplit("}", 1)[-1] == "text" and elem.text == spec["title"]:
            if elem.get("font-weight") != "700" or abs(float(elem.get("font-size")) - PT_12) > 0.01:
                raise SpecError("figure title must be 12pt bold")
            found_title = True
    if not found_title:
        raise SpecError("figure title is missing")
    del title
