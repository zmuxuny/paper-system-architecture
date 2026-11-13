# From image concept to editable figure

Use image-concept exploration first when the spatial design for a new figure is still open. For an established layout or local change, start directly from vector authoring. The default production route uses Python-authored SVG and a semantic JSON spec to establish exact text, geometry and technical relationships before native PPT export and rendered review. Explicit user requests and available tools determine which steps apply.

## Before a concept

Read the source material and identify the claim, entities, ownership, intermediate artifacts, edges, and timing. Label each supplied image by role: style reference, content source, exact asset, or edit target. A style reference does not establish a new system's scientific claims.

Use the image-generation capability available in the current environment and follow its own reference/edit rules. If none is available, create an editable vector draft and render it; state which route is being used.

## Reusable prompt

```text
Create a design preview for an editable scientific architecture/mechanism figure.
Visual language: rich but organized internal detail, nested semantic panels,
white canvas, restrained pastel headers, fine graphite lines, flat coherent
symbols, short readable labels, and a dominant core mechanism. Use meaningful
simple icons for key actors, inputs/outputs, tools and operations, paired with
labels and concrete object miniatures. Keep icon strokes, colors and scale
coherent, with enough space for readable text and distinct connections.

Reference roles:
- [reference]: stage hierarchy / internal detail / typography / composition

Verified content:
- Claim: [one sentence]
- Objects and owners: [entities and parent systems]
- Main path: [input → operation → intermediate artifact → output]
- Mechanism to expand: [structure and what actually changes]
- Timing and feedback: [one-time steps, repeated steps, availability of state]
- Exact labels and interfaces: [verified short strings]
- Connections: [source, target, data/control, trigger]

Intended use: [standalone research figure / presentation slide].
Output format: [SVG / editable PPT / draw.io], independent of intended use.
Composition: [aspect ratio and output context], prominent [core region],
compact [supporting regions], reserved space for [feedback/branch routes].
For a presentation, use a left diagram and right round-bullet takeaways.
For a standalone figure, organize the figure area around the mechanism.
Show concrete structures, artifacts, and state transitions supported by the
content. Keep labels and necessary example text readable. Put explanatory
sentences in presentation takeaways or a standalone figure's caption/surrounding
text; do not add tiny explanatory sentences below modules or squeeze summary
prose into the drawing.

Invariants: [required truths]. Use illustrative examples rather than invented
measurements. Avoid extra actors, unsupported stages, decorative numbers,
glossy 3D, mechanical ornament, and generic equal-card layouts.
```

## After the concept

Inspect useful spatial decisions and unwanted inventions. Show a complete preview early. A further generation should resolve a specific design question; repeated image generation is a poor tool for exact lettering and endpoint corrections.

Rebuild the selected composition with native text and editable vector objects. Recheck every label and connection against the semantic map. This is deliberate reconstruction, not automatic tracing or proof that the image model understood the mechanism.

For PowerPoint, preserve native editable diagram text, shapes and connectors in both uses, including the left diagram on a presentation slide. Keep presentation takeaways editable too.

Render the final SVG, PPT, or draw.io output and inspect it at its intended size. Keep a concept preview distinct from a finished deliverable. Fix actual errors and preserve accepted regions; no finding or iteration quota applies.
