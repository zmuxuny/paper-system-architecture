# Native PowerPoint export in the default route

Use Python-authored SVG plus a semantic JSON spec and native PowerPoint export as the default production route. Image-concept exploration precedes vector authoring when the spatial design is still open. Author the SVG with native text, paths, primitive shapes, and stable semantic groups, including editable vector icons. The bundled adapter `scripts/export_native_deck.py` combines pages using an installed [FigGenie](https://github.com/Sleepy-Avacado/FigGenie-paper-diagram-skill) converter. FigGenie is a separate dependency and is not vendored here. SVG-only and draw.io requests follow their requested formats.

Choose composition by intended use before exporting. A standalone research figure may use PowerPoint as its editable vector source and should retain its figure layout. A presentation defaults to a large left diagram and right-hand round-bullet takeaways. In both cases the diagram's text, shapes and connectors must be native editable objects; the presentation's right-hand text must be editable too. The export format does not determine the page layout.

## Requirements

- Python 3.10 or later, `python-pptx` and `lxml`.
- A compatible FigGenie installation with `scripts/svg2pptx.py` and its own supporting files/dependencies. Read its `references/pptx-export.md`.
- Available fonts appropriate to the content; a CJK-capable face for Chinese.
- PowerPoint or another renderer such as LibreOffice for checking the actual result.

Install this repository's optional Python dependencies with `pip install -r requirements-export.txt` from the repository root. The design skill and SVG examples work without this export setup.

## Export

From the repository root:

```bash
python skills/paper-system-architecture/scripts/export_native_deck.py \
  skills/paper-system-architecture/assets/examples/evidence-atlas-overview.svg \
  skills/paper-system-architecture/assets/examples/evidence-atlas-provenance.svg \
  --specs skills/paper-system-architecture/assets/examples/evidence-atlas-overview.json \
          skills/paper-system-architecture/assets/examples/evidence-atlas-provenance.json \
  --converter-dir /path/to/figgenie-paper-diagram/scripts \
  --output build/evidence-atlas.pptx --title 'Evidence Atlas'
```

If both skills are installed beside one another, the adapter can discover the sibling converter. Use `--notes notes.json` for an array of public speaker-note strings, one per page. Set `--latin` and `--cjk` for the fonts available in your environment.

The adapter supports positive, zero-origin SVG viewBoxes with a common aspect ratio. It creates native PowerPoint objects through the converter, preserves grouping, and removes theme shadows for the flat visual profile. The supported SVG subset depends on the installed converter; inspect its warnings and documentation.

## Export issues to check

| Issue | Action |
| --- | --- |
| Scaled icons have unexpectedly heavy strokes | Compare SVG and native PPT. `--resolve-nested-strokes` is an opt-in compatibility adjustment for converters that scale geometry but leave line styling in user units. Check the installed converter first to avoid double scaling. |
| Theme adds shadows | Inspect native effect references and the rendered result; the adapter clears outer shadows. |
| Font substitution changes line length | Choose installed fonts, preserve text as text, and inspect final-format rendering. |
| A contained symbol is reported as an overlapping peer | Correct the semantic group/spec hierarchy before relaxing geometry checks. |
| One page passes automated checks | Establish the checker's coverage and inspect every delivered page. |

Keep a fresh export-tree copy when resolving strokes; leave the authoring SVG unchanged. The included examples use direct coordinates and do not need the compatibility flag.

## Inspect the delivered format

For example, with a separate LibreOffice profile:

```bash
libreoffice -env:UserInstallation=file:///tmp/paper-figure-review \
  --headless --convert-to pdf --outdir build build/evidence-atlas.pptx
pdftoppm -scale-to 1920 -png build/evidence-atlas.pdf build/page
```

Open every rendered page. Check arrow endpoints, readable text, border clearance, line separation, meaningful icon differences and page completeness. Verify the diagram itself contains editable text, shapes and connectors, including the left diagram on a presentation slide; editable right-hand text alone is insufficient. Correct observed issues and finish when the requested result is satisfied.
