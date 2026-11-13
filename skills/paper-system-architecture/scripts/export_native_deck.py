#!/usr/bin/env python3
"""Combine SVG research figures into editable native PowerPoint slides.

Uses a separately installed FigGenie converter. Inspect converter behavior
before enabling the optional nested-stroke compatibility adjustment.
"""
import argparse
import json
import math
import re
import sys
from pathlib import Path



def resolve_strokes(element, converter, matrix=(1, 0, 0, 1, 0, 0)):
    matrix = converter.mmul(matrix, converter.parse_transform(element.get('transform', '')))
    sx, sy = converter.scales(matrix)
    scale = math.sqrt(sx * sy)
    if element.get('stroke-width') is not None:
        element.set('stroke-width', str(float(element.get('stroke-width')) * scale))
    dash = element.get('stroke-dasharray')
    if dash and dash != 'none':
        element.set('stroke-dasharray', ' '.join(
            str(float(value) * scale) for value in re.split(r'[\s,]+', dash.strip())))
    for child in element:
        resolve_strokes(child, converter, matrix)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('svgs', type=Path, nargs='+')
    parser.add_argument('--specs', type=Path, nargs='+', required=True)
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--notes', type=Path, help='JSON array: one public speaker-note string per page')
    parser.add_argument('--width-inches', type=float, default=16)
    parser.add_argument('--latin', default='Arial')
    parser.add_argument('--cjk', default='Microsoft YaHei')
    parser.add_argument('--title', default='Research architecture')
    parser.add_argument('--author', default='')
    parser.add_argument('--resolve-nested-strokes', action='store_true')
    parser.add_argument('--converter-dir', type=Path, default=(
        Path(__file__).resolve().parents[2] / 'figgenie-paper-diagram' / 'scripts'))
    args = parser.parse_args()
    if len(args.svgs) != len(args.specs):
        parser.error('Supply one spec per SVG.')
    if args.width_inches <= 0:
        parser.error('Slide width must be positive.')
    if not (args.converter_dir / 'svg2pptx.py').is_file():
        parser.error('svg2pptx.py not found; install figgenie-paper-diagram or set --converter-dir.')
    sys.path.insert(0, str(args.converter_dir))
    import svg2pptx
    from lxml import etree
    from pptx import Presentation
    from pptx.util import Pt

    notes = json.loads(args.notes.read_text()) if args.notes else [''] * len(args.svgs)
    if not isinstance(notes, list) or len(notes) != len(args.svgs) or not all(isinstance(n, str) for n in notes):
        parser.error('Notes must be an array of strings, one per SVG.')

    prs = Presentation()
    aspect = None
    for svg, spec_path, note in zip(args.svgs, args.specs, notes):
        root = etree.parse(str(svg)).getroot()
        viewbox = [float(v) for v in re.split(r'[\s,]+', root.get('viewBox', '').strip()) if v]
        if len(viewbox) != 4 or viewbox[0:2] != [0, 0] or min(viewbox[2:]) <= 0:
            parser.error(f'{svg}: this helper expects viewBox="0 0 width height".')
        width, height = viewbox[2:]
        if aspect is not None and not math.isclose(width / height, aspect, rel_tol=1e-6):
            parser.error('All pages must share an aspect ratio.')
        aspect = width / height
        scale = args.width_inches * 72 / width
        prs.slide_width = Pt(width * scale)
        prs.slide_height = Pt(height * scale)
        if args.resolve_nested_strokes:
            resolve_strokes(root, svg2pptx)
        spec = json.loads(spec_path.read_text())
        cv = svg2pptx.Converter(root, spec, scale, args.latin, args.cjk,
                               'text', None, base_dir=svg.parent)
        cv.prs = prs
        cv.slide = prs.slides.add_slide(prs.slide_layouts[6])
        cv.SH = cv.slide.shapes
        cv.run(group=True)
        for element in list(cv.slide._element.iter()):
            if element.tag == '{http://schemas.openxmlformats.org/drawingml/2006/main}effectRef':
                element.set('idx', '0')
            elif element.tag == '{http://schemas.openxmlformats.org/drawingml/2006/main}outerShdw':
                element.getparent().remove(element)
        cv.slide.notes_slide.notes_text_frame.text = note
    props = prs.core_properties
    props.title = args.title
    props.author = args.author
    props.last_modified_by = args.author
    props.comments = ''
    args.output.parent.mkdir(parents=True, exist_ok=True)
    prs.save(args.output)
    print(f'{args.output} ({len(prs.slides)} editable slides)')


if __name__ == '__main__':
    main()
