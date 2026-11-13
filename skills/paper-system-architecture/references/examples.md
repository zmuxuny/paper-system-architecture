# Examples and visual study

Open the images when using the skill. Reading their filenames is not a substitute for inspecting the composition.

## Original illustrative examples

The bundled **Evidence Atlas** examples use fictional documents to demonstrate common retrieval and citation concepts. They are authored for this repository and carry the repository's MIT license. They are not a research result or performance claim.

| Example | Files | What to study |
| --- | --- | --- |
| Architecture | [SVG](../assets/examples/evidence-atlas-overview.svg), [PNG](../assets/examples/evidence-atlas-overview.png), [spec](../assets/examples/evidence-atlas-overview.json) | Separate indexing and query-time responsibilities; visible document/chunk/index objects; compact sources; large core; readable takeaways |
| Mechanism | [SVG](../assets/examples/evidence-atlas-provenance.svg), [PNG](../assets/examples/evidence-atlas-provenance.png), [spec](../assets/examples/evidence-atlas-provenance.json) | One concrete span carried through document, chunk record, evidence and citation; stable object identity; steps with distinct visual anatomy |

Use the organization and visual grammar. Replace the domain, labels, structures and algorithms with the new system's actual content.

The source generator is `tools/build_examples.py` in the repository root. It uses ordinary SVG primitives and CairoSVG for the previews; the skill's design instructions do not depend on running it.

## Public paper references

These external papers offer useful examples of organized information density:

- [HarnessFix](https://arxiv.org/abs/2606.06324): stages with distinct agents, records, specifications and output artifacts.
- [GraphTracer, v1](https://arxiv.org/abs/2510.10581v1): a dominant worked graph, smaller supporting regions, and local mechanism illustrations. The paper was later withdrawn; this link is a visual-composition reference.
- [CHIEF](https://arxiv.org/abs/2602.23701): asymmetric composition, repeated internal structures and a compact relation legend.

Follow the links to inspect the authors' figures. External figures are not bundled or covered by this repository's license. Study their structure and hierarchy; their algorithms, terminology, exact geometry and graphical assets remain specific to those papers.
