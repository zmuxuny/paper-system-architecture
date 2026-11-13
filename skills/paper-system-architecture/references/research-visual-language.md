# Mechanism-explicit research figures

The visual aim is simple: **understand the architecture at a glance, follow the mechanism at a closer look, and find concrete technical detail when inspecting a component.** In Chinese, a useful description is “机制展开式科研架构图”. This is a descriptive phrase, not a formal design movement.

## Three levels of reading

| Scale | What the reader sees | How to build it |
| --- | --- | --- |
| Whole figure | Major responsibilities and one dominant idea | Unequal region sizes; coherent headers; a visible primary path |
| Region | Inputs, operations, artifacts, and ownership | Nested groups; short labels; explicit intermediate objects |
| Local detail | What changes and how | Miniature data structures, spans, sequences, highlighted edges, before/after states |

An abstract “process” box becomes informative when the actual input, operation, and resulting artifact are visible. Add only detail supported by the system. Example data can be synthetic, but identify it as an illustration rather than a measurement.

## Composition

Allocate space by explanatory importance. A narrow context band, a dominant mechanism, and a compact result region often work well. A three-stage pipeline, an asymmetric overview, or an object-to-state walkthrough may fit better; let the content decide.

Keep groups compact internally and separate them with whitespace. Use a boundary when it establishes ownership or scope. An outline around every label usually weakens the hierarchy.

Reserve channels for cross-region edges and feedback before placing small components. A route that needs many detours often indicates a layout problem.

## White research profile

Use a white canvas, dark graphite text, pale semantic header bands, thin colored boundaries, and flat line symbols. Large fields stay quiet so internal structure remains visible.

| Role | Accent | Light surface |
| --- | --- | --- |
| Blue | `#366B9A` | `#E7F1F8` |
| Green | `#587B4D` | `#EAF2E2` |
| Purple | `#80659C` | `#EEE7F5` |
| Gold | `#B58B54` | `#FBF0D4` |
| Warm input/context | `#B58B54` | `#FAEDDE` |
| Text / secondary text | `#26313B` / `#57616D` | `#FFFFFF` |
| Neutral structure | `#929DA8` | `#F5F7F9` |
| Local warning or changed object | `#D56D67` | Use sparingly |

Assign colors to responsibilities or object families, then preserve that meaning. A new project can assign different semantics; a color is not permanently tied to an algorithm.

### Geometry and type for a 1600 × 900 slide

These are starting values for a presentation canvas, not print-size requirements.

| Element | Starting value |
| --- | --- |
| Outer margin | 36–44 logical units |
| Title | 34–38 |
| Panel heading | 24–26 |
| Component labels | 22–24 |
| Compact supporting labels | About 20; test readability |
| Right-column heading / body | 28 / 24–25 |
| Panel header height | About 42 |
| Outline / principal edge | 1.1–1.5 / 1.6–2.0 |
| Outer / inner corner radius | 8–10 / 4–8 |
| Parallel long edge to boundary | About 20–30 units of separation |

For a slide with takeaways, give roughly three quarters of the usable width to the diagram. Align the first bullet with the diagram's upper region. Use ordinary round bullets and concise explanations. Page count, logos, and institutions come from the actual brief.

For a paper figure, start from the venue's dimensions and evaluate at final print size. Scale the composition and reflow labels; simply shrinking a slide makes its details unreadable.

## Alternate Mineral Paper profile

A softly tinted field can suit a less stark presentation. Keep warm neutral modules and use color primarily on semantic rails, headers, or selected routes.

| Role | Color |
| --- | --- |
| Paper / module | `#E8ECF1` / `#F7F4EE` |
| Text / structure | `#20242A` / `#545B66` |
| Controller field | `#DDD9EB` |
| Blue / green | `#3F88C5` / `#4E9B68` |
| Gold / coral | `#D19A32` / `#D45D52` |

Use the selected profile consistently. Change the palette only when the brief or observed contrast warrants it.

## Shapes and icons carry meaning

- Use a document or code sheet for a produced artifact, an enclosing panel for ownership, and a distinct shape for a decision.
- Simple line icons should explain a concept. A face, robot, or decorative illustration is useful only when it represents a real actor in the system.
- Repeated objects keep their geometry and color. Highlight the changed part rather than redesigning the entire object.
- Show a source span, altered edge, new buffer state, or another concrete change when explaining a transformation.
- Use software metaphors as software. Avoid unnecessary mechanical housings, screws, or metallic effects.

Avoid decorative KPI cards, glossy effects, arbitrary badges, and equal-size colored cards with unrelated roles. Increase density by revealing mechanisms, not by adding paragraphs or shrinking text.

## Routing and local revision

Give every edge a real endpoint. Use a straight path when objects align; bend only for a reason. Put line labels near the relevant segment with clear padding. Shared line segments imply shared flow; separate unrelated edges.

When the user requests a local change, preserve approved areas. Trace moved edges again, check the full page for regressions, and finish when the new render satisfies the request.
