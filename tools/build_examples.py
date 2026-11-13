#!/usr/bin/env python3
"""Build original illustrative SVG figures and PNG previews for this repository."""
from contextlib import contextmanager
from html import escape
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'skills' / 'paper-system-architecture' / 'assets' / 'examples'
INK = '#26313B'
MUTED = '#57616D'
GRAY = '#929DA8'
BLUE, PB = '#366B9A', '#E7F1F8'
GREEN, PG = '#587B4D', '#EAF2E2'
PURPLE, PP = '#80659C', '#EEE7F5'
GOLD, PY = '#B58B54', '#FBF0D4'
WHITE = '#FFFFFF'


class Figure:
    def __init__(self, name, title, kind):
        self.name = name
        self.parts = [
            '<svg xmlns="http://www.w3.org/2000/svg" width="1600" height="900" '
            'viewBox="0 0 1600 900" font-family="Arial, DejaVu Sans, sans-serif" '
            f'font-size="22" fill="{INK}" stroke-linejoin="round" stroke-linecap="round">',
            f'<title>{escape(title)}</title>',
            '<desc>Original illustrative document system with synthetic content.</desc>',
            '<defs>',
        ]
        for name_, color in [('ink', INK), ('blue', BLUE), ('green', GREEN), ('purple', PURPLE)]:
            self.parts.append(f'<marker id="arrow-{name_}" viewBox="0 0 10 8" '
                              f'refX="9" refY="4" markerWidth="7" markerHeight="6" orient="auto">'
                              f'<path d="M0 0 L10 4 L0 8 Z" fill="{color}"/></marker>')
        self.parts.append('</defs>')
        self.spec = {'meta': {'id': name, 'title': title, 'family': 'systems',
                             'kind': kind, 'figure_kind': 'whole-system' if kind == 'architecture' else 'mechanism',
                             'column': 'double', 'template': 'custom', 'direction': 'mixed',
                             'palette': 'custom', 'step_markers': 'none'},
                     'nodes': [], 'containers': [], 'annotations': []}
        self.rect(0, 0, 1600, 900, WHITE, 'none')
        with self.group('title', title, 'annotations'):
            self.text(40, 64, title, 36, bold=True)
        self.text(1560, 61, 'ILLUSTRATIVE SYSTEM', 16, MUTED, anchor='end')
        self.line(40, 94, 1560, 94, '#D9DFE4', 1)

    @contextmanager
    def group(self, name, label, kind='nodes'):
        prefix = {'nodes': 'n', 'containers': 'c', 'annotations': 'a'}[kind]
        self.parts.append(f'<g id="{prefix}:{name}">')
        self.spec[kind].append({'id': name, 'label': label})
        yield
        self.parts.append('</g>')

    def rect(self, x, y, w, h, fill=WHITE, stroke=GRAY, r=6, dash=None):
        extra = f' stroke-dasharray="{dash}"' if dash else ''
        self.parts.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" '
                          f'fill="{fill}" stroke="{stroke}" stroke-width="1.3"{extra}/>')

    def text(self, x, y, value, size=22, color=INK, bold=False, anchor='start'):
        self.parts.append(f'<text x="{x}" y="{y}" font-size="{size}" fill="{color}" '
                          f'font-weight="{"bold" if bold else "normal"}" text-anchor="{anchor}">{escape(value)}</text>')

    def line(self, x1, y1, x2, y2, color=INK, width=1.7, arrow=None, dash=None):
        extra = (f' marker-end="url(#arrow-{arrow})"' if arrow else '')
        extra += f' stroke-dasharray="{dash}"' if dash else ''
        self.parts.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" '
                          f'stroke="{color}" stroke-width="{width}"{extra}/>')

    def path(self, data, color=INK, width=1.7, fill='none', arrow=None):
        extra = f' marker-end="url(#arrow-{arrow})"' if arrow else ''
        self.parts.append(f'<path d="{data}" fill="{fill}" stroke="{color}" stroke-width="{width}"{extra}/>')

    def circle(self, x, y, radius, fill=WHITE, stroke=INK):
        self.parts.append(f'<circle cx="{x}" cy="{y}" r="{radius}" fill="{fill}" '
                          f'stroke="{stroke}" stroke-width="1.4"/>')

    def panel(self, name, title, x, y, w, h, pale, accent):
        with self.group(name, title, 'containers'):
            self.rect(x, y, w, h, WHITE, accent, 9)
            self.path(f'M{x+9} {y} H{x+w-9} Q{x+w} {y} {x+w} {y+9} '
                      f'V{y+43} H{x} V{y+9} Q{x} {y} {x+9} {y} Z',
                      'none', 0, pale)
            self.text(x+w/2, y+29, title, 24, bold=True, anchor='middle')

    def doc(self, x, y, width=78, height=92, label='', color=BLUE):
        self.path(f'M{x} {y} H{x+width-17} L{x+width} {y+17} V{y+height} H{x} Z', INK, 1.4, WHITE)
        self.path(f'M{x+width-17} {y} V{y+17} H{x+width}', INK, 1.1)
        start = min(31, height*.34)
        step = min(12, (height-start-12)/3)
        for i, ratio in enumerate((.58, .74, .49, .66)):
            self.line(x+12, y+start+i*step, x+12+(width-24)*ratio, y+start+i*step,
                      color if i == 1 else GRAY, 1.8)
        if label:
            self.text(x+width/2, y+height+26, label, 20, color, bold=True, anchor='middle')

    def check(self, x, y):
        self.circle(x, y, 11, '#F6FAF3', GREEN)
        self.path(f'M{x-6} {y} L{x-1} {y+5} L{x+7} {y-6}', GREEN, 1.8)

    def bullets(self, rows):
        for index, (y, heading, body) in enumerate(rows):
            with self.group(f'takeaway-{index}', heading, 'annotations'):
                self.circle(1241, y-9, 4, BLUE, 'none')
                self.text(1260, y, heading, 26, bold=True)
                for j, line in enumerate(body):
                    self.text(1260, y+41+j*34, line, 23)

    def finish(self):
        self.text(40, 873, 'EVIDENCE ATLAS  /  fictional documents · original teaching example', 17, MUTED)
        self.text(1560, 873, 'Paper System Architecture', 17, MUTED, anchor='end')
        self.parts.append('</svg>')
        OUT.mkdir(parents=True, exist_ok=True)
        svg = OUT / f'{self.name}.svg'
        svg.write_text('\n'.join(self.parts), encoding='utf-8')
        svg.with_suffix('.json').write_text(json.dumps(self.spec, indent=2), encoding='utf-8')
        import cairosvg
        cairosvg.svg2png(url=str(svg), write_to=str(svg.with_suffix('.png')), output_width=1920, output_height=1080)
        print(svg.relative_to(ROOT))


def overview():
    f = Figure('evidence-atlas-overview', 'Evidence Atlas: documents to cited answers', 'architecture')
    f.panel('inputs', 'Inputs', 40, 140, 190, 660, '#FAEDDE', GOLD)
    f.panel('indexing', 'Index construction · offline', 270, 140, 910, 255, PG, GREEN)
    f.panel('retrieval', 'Evidence-grounded response · online', 270, 450, 910, 350, PB, BLUE)

    with f.group('documents', 'Versioned source documents'):
        f.doc(75, 220, 78, 96, color=PURPLE)
        f.doc(116, 242, 78, 96, 'D2', GREEN)
        f.text(93, 353, 'D1', 20, PURPLE, bold=True, anchor='middle')
        f.text(135, 394, 'Stable IDs', 22, bold=True, anchor='middle')
        f.text(135, 426, 'Versions', 21, MUTED, anchor='middle')
        f.text(135, 457, 'Permissions', 21, MUTED, anchor='middle')
    with f.group('question', 'User question'):
        f.rect(59, 539, 152, 134, PP, PURPLE)
        f.text(135, 573, 'Question', 23, bold=True, anchor='middle')
        f.text(135, 614, 'How are sources', 18, anchor='middle')
        f.text(135, 643, 'kept traceable?', 18, anchor='middle')
        f.text(135, 727, 'Query-time input', 19, MUTED, anchor='middle')

    with f.group('segment', 'Parse and segment documents'):
        f.rect(292, 205, 231, 166, '#F8FBF5', GREEN)
        f.text(407, 237, 'Parse & segment', 23, bold=True, anchor='middle')
        f.doc(309, 257, 49, 64)
        f.line(370, 289, 392, 289, arrow='ink')
        for j, (label, color) in enumerate([('c01', PP), ('c07', PB), ('c02', PY)]):
            f.rect(404, 258+j*29, 96, 23, color, GRAY, 3)
            f.text(452, 275+j*29, label, 16, anchor='middle')
        f.text(407, 354, 'Text + source spans', 19, MUTED, anchor='middle')
    with f.group('embedding', 'Encode chunk text into vectors'):
        f.rect(562, 205, 230, 166, '#F8FBF5', GREEN)
        f.text(677, 237, 'Encode chunks', 23, bold=True, anchor='middle')
        for row, label in enumerate(('c01', 'c07', 'c02')):
            f.text(584, 271+27*row, label, 17, MUTED)
            for col in range(6):
                f.rect(627+23*col, 253+27*row, 19, 19,
                       (PB, PP, PG, '#C5D9E5')[(row+col)%4], GRAY, 1)
        f.text(677, 354, 'Embeddings + IDs', 19, MUTED, anchor='middle')
    with f.group('index', 'Store searchable chunks and provenance'):
        f.rect(831, 205, 327, 166, '#F8FBF5', GREEN)
        f.text(994, 237, 'Searchable index', 23, bold=True, anchor='middle')
        f.line(849, 248, 1138, 248, GRAY, 1)
        f.text(851, 274, 'chunk', 17, MUTED)
        f.text(932, 274, 'vector', 17, MUTED)
        f.text(1031, 274, 'source span', 17, MUTED)
        for row, (chunk, span) in enumerate((('c01', 'D1: L1–2'), ('c07', 'D2: L3–4'))):
            f.text(851, 305+29*row, chunk, 18)
            for col in range(4):
                f.rect(932+17*col, 290+29*row, 13, 16, (PB, PG, PP, PY)[col], GRAY, 1)
            f.text(1031, 305+29*row, span, 18)

    f.line(231, 287, 290, 287, arrow='ink')
    f.line(524, 287, 560, 287, GREEN, arrow='green')
    f.line(793, 287, 829, 287, GREEN, arrow='green')
    f.path('M995 372 V416 H407 V511', GREEN, arrow='green')
    f.text(744, 438, 'indexed chunks + provenance', 18, GREEN, anchor='middle')

    with f.group('search', 'Encode query and retrieve chunks'):
        f.rect(292, 513, 231, 257, WHITE, BLUE)
        f.text(407, 548, 'Search', 24, bold=True, anchor='middle')
        f.rect(310, 566, 194, 47, PB, BLUE, 4)
        f.text(407, 596, 'Query embedding', 19, BLUE, bold=True, anchor='middle')
        f.line(407, 614, 407, 632, BLUE, arrow='blue')
        for j, name in enumerate(('D2:c07', 'D1:c01', 'D2:c02')):
            f.rect(310, 640+j*34, 194, 27, [PG, PB, PP][j], GRAY, 3)
            f.text(321, 659+j*34, name, 18)
            f.line(411, 654+j*34, 482-j*14, 654+j*34, [GREEN, BLUE, PURPLE][j], 4)
    with f.group('evidence', 'Assemble selected evidence with source identifiers'):
        f.rect(562, 513, 230, 257, WHITE, BLUE)
        f.text(677, 548, 'Evidence pack', 24, bold=True, anchor='middle')
        for j, (tag, title) in enumerate((('[1]', 'D2 · lines 3–4'), ('[2]', 'D1 · lines 1–2'))):
            yy = 571+j*83
            f.rect(579, yy, 196, 69, PG if j == 0 else PB, GRAY, 4)
            f.text(590, yy+24, tag, 20, GREEN if j == 0 else BLUE, bold=True)
            f.text(630, yy+24, title, 17)
            f.line(592, yy+42, 754, yy+42, GRAY, 1.4)
            f.line(592, yy+54, 729, yy+54, GRAY, 1.4)
        f.text(677, 755, 'Excerpt + citation ID', 18, MUTED, anchor='middle')
    with f.group('response', 'Draft answer and check citation targets'):
        f.rect(831, 513, 327, 257, WHITE, BLUE)
        f.text(994, 548, 'Draft & check citations', 23, bold=True, anchor='middle')
        f.rect(850, 571, 289, 70, PB, GRAY, 4)
        f.text(866, 598, 'Source spans stay attached', 20)
        f.text(866, 626, 'to retrieved evidence. [1]', 20)
        f.line(994, 642, 994, 664, BLUE, arrow='blue')
        f.check(871, 688)
        f.text(894, 694, 'IDs · versions · line ranges', 18)
        f.line(994, 701, 994, 716, GREEN, arrow='green')
        f.rect(850, 718, 289, 34, PG, GREEN, 4)
        f.text(994, 742, 'Answer with citations', 20, GREEN, bold=True, anchor='middle')

    f.line(212, 604, 290, 604, PURPLE, arrow='purple')
    f.line(524, 637, 560, 637, BLUE, arrow='blue')
    f.line(793, 637, 829, 637, BLUE, arrow='blue')
    f.bullets([
        (218, 'Visible structure', ['Documents become', 'chunks, vectors,', 'and source records.']),
        (440, 'Distinct phases', ['Index documents offline;', 'retrieve evidence for', 'each incoming question.']),
        (662, 'Traceable evidence', ['Carry stable source', 'identifiers into', 'the cited answer.']),
    ])
    f.finish()


def provenance():
    f = Figure('evidence-atlas-provenance', 'Evidence Atlas: a citation is a traceable span', 'mechanism')
    f.panel('source-region', '1 · Source document', 40, 140, 345, 660, '#FAEDDE', GOLD)
    f.panel('chunk-region', '2 · Chunk + provenance', 420, 140, 345, 660, PG, GREEN)
    f.panel('citation-region', '3 · Evidence to answer', 800, 140, 380, 660, PB, BLUE)

    with f.group('source', 'A fictional source with stable lines and version'):
        f.rect(62, 209, 301, 484, WHITE, INK, 5)
        f.text(84, 246, 'D2 · notes.md', 24, bold=True)
        f.rect(274, 223, 65, 32, PP, PURPLE, 4)
        f.text(306, 246, 'v2', 20, PURPLE, bold=True, anchor='middle')
        f.line(83, 269, 340, 269, GRAY, 1)
        lines = [('01', 'A source has a stable ID.'),
                 ('02', 'Text is split into chunks.'),
                 ('03', 'Each chunk retains'),
                 ('04', 'its source line range.'),
                 ('05', 'A citation names that span.'),
                 ('06', 'Updates create a version.')]
        f.rect(74, 367, 277, 107, PG, GREEN, 4)
        for j, (num, text) in enumerate(lines):
            y = 309+j*52
            f.text(86, y, num, 18, GRAY)
            f.text(119, y, text, 18)
        f.line(83, 616, 338, 616, GRAY, 1)
        f.text(84, 649, 'Selected span: lines 3–4', 19, GREEN, bold=True)
        f.text(212, 741, 'Preserve document identity', 21, GOLD, bold=True, anchor='middle')

    with f.group('record', 'Chunk c07 preserves source D2 version v2 lines 3 to 4'):
        f.rect(442, 209, 301, 211, WHITE, GREEN)
        f.text(465, 244, 'Chunk c07', 25, bold=True)
        f.line(464, 258, 721, 258, GRAY, 1)
        for j, (key, value) in enumerate((('document', 'D2'), ('version', 'v2'), ('line range', '3–4'), ('chunk ID', 'c07'))):
            f.text(464, 292+j*33, key, 19, MUTED)
            f.text(720, 292+j*33, value, 21, GREEN, bold=True, anchor='end')
        f.rect(442, 457, 301, 147, PG, GREEN)
        f.text(464, 492, 'Text payload', 22, bold=True)
        f.text(464, 537, 'Each chunk retains', 22)
        f.text(464, 572, 'its source line range.', 22)
        f.rect(442, 650, 301, 93, WHITE, GREEN, 6, '5 4')
        f.text(592, 683, 'One linked record', 23, GREEN, bold=True, anchor='middle')
        f.text(592, 718, 'text + source coordinates', 20, MUTED, anchor='middle')
        f.line(592, 421, 592, 455, GREEN, arrow='green')
        f.line(592, 605, 592, 648, GREEN, arrow='green')

    with f.group('evidence-citation', 'Select evidence and attach a resolvable citation'):
        f.rect(822, 209, 336, 126, WHITE, BLUE)
        f.text(845, 244, 'Selected evidence [1]', 23, bold=True)
        f.text(845, 285, 'D2 · v2 · lines 3–4', 22, BLUE)
        f.text(845, 316, 'Chunk c07', 19, MUTED)
        f.line(990, 336, 990, 365, BLUE, arrow='blue')
        f.rect(822, 367, 336, 117, PB, BLUE)
        f.text(845, 401, 'Draft statement', 23, bold=True)
        f.text(845, 439, 'A chunk keeps its source', 21)
        f.text(845, 469, 'line range. [1]', 21)
        f.line(990, 485, 990, 518, BLUE, arrow='blue')
        f.rect(822, 520, 336, 138, WHITE, BLUE)
        f.text(845, 553, 'Resolve citation target', 22, bold=True)
        for j, label in enumerate(('Document and version exist', 'Lines 3–4 identify the span')):
            f.check(845, 586+j*39)
            f.text(867, 593+j*39, label, 18)
        f.line(990, 659, 990, 691, GREEN, arrow='green')
        f.rect(822, 693, 336, 50, PG, GREEN)
        f.text(990, 725, 'Answer + source link [1]', 23, GREEN, bold=True, anchor='middle')

    f.path('M364 420 H402 V315 H440', GREEN, arrow='green')
    f.path('M744 531 H782 V272 H820', BLUE, arrow='blue')
    f.bullets([
        (218, 'Identity persists', ['The same document,', 'version and line span', 'travel with the text.']),
        (440, 'Change is concrete', ['A highlighted span', 'becomes a structured', 'evidence record.']),
        (662, 'Meaningful detail', ['Every small object', 'helps explain the', 'citation mechanism.']),
    ])
    f.finish()


if __name__ == '__main__':
    overview()
    provenance()
