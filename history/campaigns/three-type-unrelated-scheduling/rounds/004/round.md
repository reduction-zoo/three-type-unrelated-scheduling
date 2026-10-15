# Round 4: Literature check for arithmetic saturation

## Plan

Investigate whether two-length scheduling algorithms or configuration formulations offer an arithmetic mechanism beyond fixed-fill binary selectors. Read the primary two-length paper and the relevant configuration-kernel statement; distinguish identical processing lengths from unrelated machine-dependent times. Scope: these two papers and one targeted primary-source search for exact-load three-type constructions. Completion: identify an applicable mechanism or record the precise mismatch. This is one literature attempt, not a reduction candidate. Prior rounds rule out the two displayed one-sided constructions; they do not rule out arithmetic saturation.

## Evidence and diagnosis

Search date: 2026-09-16. Read McCormick, Smallwood and Spieksma (2001), [author PDF](https://feb.kuleuven.be/public/u0037710/papers/mor2001paper.pdf), Sections 4–5 and 7, pp. 40–43 and 47. Section 5 explicitly embeds unrelated machines in its multi-resource model and Theorem 5.1 states a polynomial algorithm. This is a published statement, not an independently audited implementation or proof. The 2025 paper cites the uniform-machine consequence; that narrower citation does not itself contradict the stronger 2001 statement. No correction was located by queries `"McCormick" "unrelated" "incorrect"`, `"McCormick" "Spieksma" "erratum" scheduling`, and `"Complexity of scheduling few types" "McCormick"`. Coverage remains incomplete.

Section 7 supplies a useful three-type counterexample: two identical machines, lengths (6,10,15), counts (4,2,1), deadline 30 have a fractional configuration solution but no integer schedule. This supports testing divisibility rather than one-sided capacity. It is an existing example, not a new result.

Read Knop and Koutecký (2022), [ESA paper](https://drops.dagstuhl.de/storage/00lipics/lipics-vol244-esa2022/LIPIcs.ESA.2022.73/LIPIcs.ESA.2022.73.pdf), Theorem 2 and the informal Theorem 3, p. 73:3. Its compression depends on processing magnitudes and machine kinds as well as type count. It does not provide the requested three-type hardness construction. Do not pursue its parameterized output as the campaign theorem.

The initial search `"unrelated" "three" "job types" scheduling exact` found the existing 2025 hardness paper but no applicable new construction. Actual scope: two primary papers, one initial query and three follow-up queries interpreting the first paper. Zero candidates, solver queries, or recovery calls. No execution repairs or reruns. Time/token totals unavailable.

Experience extraction: none. The applicable new information is a cited existing counterexample and an unaudited literature statement; neither is a new local construction lesson yet.

## Next action

Test exact-load divisibility on the published example and its pairwise-coprime generalization. Determine whether its nonconvexity alone supplies item selection or merely a residue obstruction. Prospects remain low and uncalibrated.
