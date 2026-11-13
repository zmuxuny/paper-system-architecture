"""Small behavioral checks for the public skill package and export CLI."""
from pathlib import Path
import json
import re
import subprocess
import sys
import unittest
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / 'skills' / 'paper-system-architecture'
SVG_NS = '{http://www.w3.org/2000/svg}'


class PackageTests(unittest.TestCase):
    def test_internal_markdown_links_resolve(self):
        for path in ROOT.rglob('*.md'):
            if '.git' in path.parts or 'build' in path.parts:
                continue
            for target in re.findall(r'\]\(([^)]+)\)', path.read_text(encoding='utf-8')):
                if '://' in target or target.startswith('#'):
                    continue
                self.assertTrue((path.parent / target.split('#')[0]).exists(), (path, target))

    def test_examples_are_self_contained_editable_vectors(self):
        svgs = sorted((SKILL / 'assets' / 'examples').glob('*.svg'))
        self.assertEqual(len(svgs), 2)
        for svg in svgs:
            root = ET.parse(svg).getroot()
            self.assertEqual(root.get('viewBox'), '0 0 1600 900')
            self.assertGreater(len(list(root.iter(SVG_NS + 'text'))), 35)
            self.assertGreater(len(list(root.iter(SVG_NS + 'path'))), 8)
            self.assertEqual(list(root.iter(SVG_NS + 'image')), [])
            ids = [e.get('id') for e in root.iter() if e.get('id')]
            self.assertEqual(len(ids), len(set(ids)))
            for el in root.iter():
                for value in el.attrib.values():
                    for linked_id in re.findall(r'url\(#([^)]*)\)', value):
                        self.assertIn(linked_id, ids)
            png = svg.with_suffix('.png').read_bytes()
            self.assertEqual(png[:8], b'\x89PNG\r\n\x1a\n')

    def test_specs_name_existing_semantic_groups(self):
        for spec_path in (SKILL / 'assets' / 'examples').glob('*.json'):
            spec = json.loads(spec_path.read_text())
            ids = {e.get('id') for e in ET.parse(spec_path.with_suffix('.svg')).iter()}
            for kind, prefix in [('nodes', 'n'), ('containers', 'c'), ('annotations', 'a')]:
                for entry in spec[kind]:
                    self.assertIn(prefix + ':' + entry['id'], ids)

    def run_export(self, *args):
        return subprocess.run([sys.executable, str(SKILL / 'scripts' / 'export_native_deck.py'), *args],
                              capture_output=True, text=True)

    def test_export_rejects_mismatched_page_specs(self):
        result = self.run_export('one.svg', 'two.svg', '--specs', 'one.json', '--output', 'unused.pptx')
        self.assertEqual(result.returncode, 2)
        self.assertIn('one spec per SVG', result.stderr)

    def test_export_reports_missing_optional_converter(self):
        result = self.run_export('one.svg', '--specs', 'one.json', '--output', 'unused.pptx',
                                 '--converter-dir', str(ROOT / 'missing-converter'))
        self.assertEqual(result.returncode, 2)
        self.assertIn('svg2pptx.py not found', result.stderr)


if __name__ == '__main__':
    unittest.main()
