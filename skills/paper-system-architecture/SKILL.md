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
- the requested medium and available space.

For each arrow, know its source, destination, meaning, and trigger. Distinguish data, control, and feedback. Ask a concise question when missing information affects correctness; continue independent work while waiting. Do not invent components to fill a composition.

## Choose a visual profile

- **White research figures and technical slides:** read [research-visual-language.md](references/research-visual-language.md), then inspect the relevant [example](references/examples.md). Use nested semantic panels, concrete internal structure, restrained pastel headers, and fine graphite lines.
- **Mineral Paper:** use the alternate palette in the same reference when a softly tinted paper field suits the request.
- **User references:** distinguish content, structure, style, geometry, and exact assets. Read their organization as well as their colors. Adaptation does not imply pixel-perfect reproduction.

Use three levels of reading: whole-system regions, local mechanisms, and concrete detail. Information density should come from meaningful objects and relationships, with enough space to distinguish them.

## Compose before routing

Allocate the core mechanism the most space; keep supporting inputs and outputs compact. Expand a key operation into the actual structure it changes: document spans, graph edges, buffers, matrices, sequences, or another domain-appropriate object.

Use containment to express ownership and aligned groups to express related responsibilities. Show a state transition with a visible difference. Give feedback and decision branches independent space before filling the canvas with boxes.

For slides, a compact title, dominant diagram, and a readable right-hand bullet column is a useful pattern. For paper figures, use the publication's final dimensions and verify at print size. Do not force slide proportions onto a narrow column.

## Explore and author

When the user requests an image concept, or a new composition benefits from visual exploration, use an available image-generation tool. Supply the verified entity/edge map and style references. Show a complete concept early, then rebuild text, shapes and connections in an editable source. Use [concept-to-vector.md](references/concept-to-vector.md) for the prompt scaffold and transition.

For an approved editable composition, make local vector changes directly. Choose the requested route:

- **SVG:** native text, paths and grouped primitives with stable semantic IDs.
- **Native PowerPoint:** create the SVG, then use an available converter. The optional multi-slide adapter and dependencies are documented in [native-powerpoint.md](references/native-powerpoint.md).
- **draw.io:** use editable XML shapes, text and connectors with an available draw.io workflow; retain actual source and target ports.

The core design workflow does not require another skill. Optional tooling must actually be available; do not describe a bitmap as native editable output.

## Make the mechanism legible

- Keep actors, operations, produced artifacts, and stored state distinguishable.
- Place interfaces inside their owning subsystem; match their names to the source material.
- Show changes with concrete examples and consistent old/new or input/output encodings.
- For parallel work, show independent progress and the point where results are consumed. Return feedback only to the stage that repeats.
- Give conditions and result objects distinct destinations. Draw a junction only for a real merge.
- Use straight edges for aligned objects. Otherwise use clean orthogonal routes with gentle bends and visible endpoints.
- Keep labels short and readable; put longer explanations beside the figure. Enlarge or reorganize content before shrinking important text.

Use colors consistently, restrained outlines, and a small coherent icon vocabulary. Match the reference's information organization rather than adding decoration.

## Refine and finish

Render the actual delivery format. Inspect the full figure for reading order and the affected regions for text, endpoints, line separation, and frame clearance. Check every delivered page; a validator that inspects one page does not establish quality for the whole deck.

Preserve approved regions while correcting the named issue. Fix observed defects and verify the change. Finish when the requested content, relations, legibility, and style are satisfied. There is no required number of iterations, defects, red-team findings, or self-score; zero findings can be a valid result.

If the same defect persists, inspect its geometry, font, renderer, or converter cause. Report a concrete remaining limitation when necessary. Deliver the requested editable formats and a clearly identified current preview.
