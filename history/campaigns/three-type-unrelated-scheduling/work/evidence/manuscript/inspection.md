# Manuscript inspection

Date: 2026-09-16. Applied research-write and how-to-technical-writing; used PDF visual inspection. The final five-page Typst manuscript matches the independently reviewed theorem and both maps. No candidate or proof implementation changed after review.

Compiled with Typst 0.15.1; final compile.txt is empty and compilation exited successfully. Rendered every page with `pdftoppm -scale-to 1400 -png manuscript.pdf evidence/manuscript/page`. Inspected all five final PNG pages. Native formulas, subscripts, product signs, captions, references and code blocks are legible and within the page bounds. Kept the second-column equation with its setup paragraph. Corrected the minimum-operator attachment in the appendix and two plot-label positions. No clipped or overlapping final content was found.

The SVG generator uses only the Python standard library and explicitly checks all five plotted integer configurations and the two retained configurations. It was rerun after label placement changes; figure-check.txt records success. The worked CLI example was executed in both modes and its witness independently checked against the actual emitted target; example.json records the result. These are writing checks, not new research rounds or enlarged verification-suite counts.

Authoring repairs: an initial patch was rejected before writing; an initial plot script found matplotlib unavailable and was replaced with direct SVG generation (figures/build-failure.txt); the first Typst compile rejected the nonnative `prod` identifier (compile-error.txt). Final native notation uses `product`. These failures did not change the mathematical construction.

The manuscript contains no invented authors or venue, and clearly states that it has not received human peer review. The literature-search coverage gaps from the independent review remain explicit in the appendix. Reused all passing reduction tests; editorial changes did not trigger another algorithm suite.
