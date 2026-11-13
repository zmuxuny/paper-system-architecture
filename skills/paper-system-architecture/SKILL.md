---
name: paper-system-architecture
description: Create editable research architecture and mechanism figures with rich structural detail, clear semantic flows, restrained colors, and readable technical-slide layouts. Use for paper overviews, method diagrams, technical proposals, and presentation figures in SVG, native PowerPoint, or draw.io. Supports reference-led image concepts followed by vector rebuilding and rendered-output checks.
---

# Paper System Architecture

Make the system's main idea visible through its structure, concrete objects, and changes of state. Preserve technical accuracy and editability.

## Understand the figure

Read the relevant project instructions and source material. Establish:

- the one-sentence claim and intended audience;
- the objects, responsibilities, inputs, intermediate artifacts, and outputs;
- the primary reading path and the mechanism worth expanding;
- ownership boundaries, timing, and any loops or independent phases;
- the intended use (standalone figure or presentation), output format, and available space.

For each arrow, know its source, destination, meaning, and trigger. Distinguish data, control, and feedback. Ask a concise question when missing information affects correctness; continue independent work while waiting. Do not invent components to fill a composition.

## Choose a visual profile

- **White research figures and technical slides:** read [research-visual-language.md](references/research-visual-language.md), then inspect the relevant [example](references/examples.md). Use nested semantic panels, concrete internal structure, restrained pastel headers, and fine graphite lines.
- **Mineral Paper:** use the alternate palette in the same reference when a softly tinted paper field suits the request.
- **User references:** distinguish content, structure, style, geometry, and exact assets. Read their organization as well as their colors. Adaptation does not imply pixel-perfect reproduction.

Use three levels of reading: whole-system regions, local mechanisms, and concrete detail. Information density should come from meaningful objects and relationships, with enough space to distinguish them.

## Compose before routing

Allocate the core mechanism the most space; keep supporting inputs and outputs compact. Expand a key operation into the actual structure it changes: document spans, graph edges, buffers, matrices, sequences, or another domain-appropriate object.

Use containment to express ownership and aligned groups to express related responsibilities. Show a state transition with a visible difference. Give feedback and decision branches independent space before filling the canvas with boxes.

Choose layout by intended use, independently of file format. A standalone research figure can use `.pptx` as its editable vector source; compose it around the mechanism and final publication dimensions, with explanations in the caption or surrounding document.

For presentation slides, default to a compact title, large left-hand diagram and right-hand round-bullet takeaways unless the brief specifies another layout. In PowerPoint, keep the left diagram's text, shapes and connectors native and editable, along with the right-hand text. Both uses require an editable diagram; a full-diagram screenshot does not meet that requirement.

## Default authoring route

Use this route by default, with the composition determined by intended use:

1. **Image concept when composition is open:** prefer an available image-generation tool to explore a new spatial design, using the verified entity/edge map and style references. If the layout is already established, proceed directly to vector authoring. Inspect a complete concept early when using this step. See [concept-to-vector.md](references/concept-to-vector.md).
2. **Vector reconstruction:** use Python to build native SVG text, shapes, paths and stable semantic groups, with a companion JSON spec. Verify labels and connections against the source; image generation is neither technical verification nor automatic vector tracing.
3. **Native PPT as the default editable export:** convert through the separately installed FigGenie engine and the bundled `scripts/export_native_deck.py` adapter into editable PowerPoint objects, unless the user requests another format. Preserve the standalone-figure or presentation layout chosen earlier. See [native-powerpoint.md](references/native-powerpoint.md) for dependencies and commands.
4. **Actual-output review:** render the PPT with LibreOffice to PDF and Poppler to PNG, inspect every page, correct observed issues in the source, and re-export. Deliver native PPT with source SVG/spec and a clearly identified preview unless the user requests a different set.

For an existing approved composition, edit the vector source and re-export; do not restart image generation for a label or connector fix. Explicit output requests take precedence: SVG-only delivery stops at a rendered SVG, and draw.io requests use an available editable draw.io workflow. If an image tool or converter is unavailable, state the missing step and use an available editable route without claiming the unavailable format was produced. The design instructions remain usable without the export dependencies.

## Make the mechanism legible

- Keep actors, operations, produced artifacts, and stored state distinguishable.
- Place interfaces inside their owning subsystem; match their names to the source material.
- Show changes with concrete examples and consistent old/new or input/output encodings.
- For parallel work, show independent progress and the point where results are consumed. Return feedback only to the stage that repeats.
- Give conditions and result objects distinct destinations. Draw a junction only for a real merge.
- Use straight edges for aligned objects. Otherwise use clean orthogonal routes with gentle bends and visible endpoints.
- Across visual profiles, keep labels, interfaces, legends and necessary worked-example text readable. Keep explanatory sentences and summary copy outside the internal mechanism drawing: use presentation takeaways or a standalone figure's caption/surrounding text. Do not add tiny explanatory sentences beneath module names or squeeze summary prose into the diagram; enlarge or reorganize the drawing instead.

Actively enrich the figure with meaningful icons for key actors, inputs/outputs, tools and operations, paired with short labels. Use a coherent flat line-icon family with consistent strokes, accent colors and scale; expand the core mechanism with concrete object miniatures and state changes. Favor SVG paths or native shapes that remain editable in PPT. Preserve text size and connection clearances; do not impose an icon quota or decorate every minor label.

## Refine and finish

Render the actual delivery format. Inspect the full figure for reading order and the affected regions for text, endpoints, line separation, and frame clearance. Check every delivered page; a validator that inspects one page does not establish quality for the whole deck.

Preserve approved regions while correcting the named issue. Fix observed defects and verify the change. Finish when the requested content, relations, legibility, and style are satisfied. There is no required number of iterations, defects, red-team findings, or self-score; zero findings can be a valid result.

If the same defect persists, inspect its geometry, font, renderer, or converter cause. Report a concrete remaining limitation when necessary. Deliver the requested editable formats and a clearly identified current preview.
