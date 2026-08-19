#!/usr/bin/env python3
"""HarfBuzz-shaped text to SVG paths. Kerned, GitHub-safe."""
import functools
import uharfbuzz as hb
from fontTools.ttLib import TTFont
from fontTools.varLib.instancer import instantiateVariableFont
from fontTools.pens.svgPathPen import SVGPathPen


@functools.lru_cache(maxsize=4)
def _load(font_path, axes_key):
    axes = dict(axes_key)
    tt = TTFont(font_path)
    if axes and "fvar" in tt:
        instantiateVariableFont(tt, axes, inplace=True)
    blob = hb.Blob(open(font_path, "rb").read())
    face = hb.Face(blob)
    font = hb.Font(face)
    if axes:
        font.set_variations(axes)
    return tt, font, tt["head"].unitsPerEm


def shape_to_paths(font_path, text, size, axes=None):
    """Returns (svg_path_elements, advance_width_px). Kerned via HarfBuzz."""
    axes_key = tuple(sorted((axes or {}).items()))
    tt, font, upem = _load(font_path, axes_key)
    scale = size / upem
    buf = hb.Buffer()
    buf.add_str(text)
    buf.guess_segment_properties()
    hb.shape(font, buf, {"kern": True, "liga": True})
    glyph_set = tt.getGlyphSet()
    glyph_order = tt.getGlyphOrder()
    x = y = 0.0
    parts = []
    for info, pos in zip(buf.glyph_infos, buf.glyph_positions):
        gname = glyph_order[info.codepoint]
        pen = SVGPathPen(glyph_set)
        glyph_set[gname].draw(pen)
        d = pen.getCommands()
        if d:
            gx = (x + pos.x_offset) * scale
            gy = (y + pos.y_offset) * scale
            parts.append(
                f'<path transform="translate({gx:.1f},{-gy:.1f}) '
                f'scale({scale:.6f},{-scale:.6f})" d="{d}"/>')
        x += pos.x_advance
        y += pos.y_advance
    return parts, x * scale
