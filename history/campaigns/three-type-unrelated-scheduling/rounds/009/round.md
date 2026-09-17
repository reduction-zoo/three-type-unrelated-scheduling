# Round 9: A scalable affine selector

## Plan

Generalize the actual (2,3,5) examples from round 7 to w=(k,k+1,2k+1), k=max a_i. For each a in [1,k], intended configurations are u=(0,2k+1-a,0), v=(a,0,k+1-a), both of objective b=(k+1)(2k+1-a). Set H=4(k+1)^2, local processing row p=H w+(2k+1-a,a,0), and capacity C=H b+a(2k+1-a). Prove that every feasible configuration has objective at most b and that the only maximizers are u and v.

Composition: normalize local capacities using their product T. Set global counts (A/2, m(2k+1)/2-A/2, m(k+1)/2-A/2). Their objective is sum b_i, which should force every machine to a local maximizing configuration. Recover selected items from rows equal to v. Scope: prove the local fiber classification; exhaustively inspect k=1..8 and a=1..k; if it passes, implement both maps and use the unchanged eight prepared source cases. Handle empty and odd-total sources explicitly. This is one construction hypothesis; implementation repairs remain in this round.

## Evidence and diagnosis

The local selector works for all k>=1 and 1<=a<=k. The general proof reduces the objective equality modulo k+1: x+z is 0, k+1, or 2(k+1). The last case is excluded by the perturbation; the middle case has exactly one feasible endpoint. Global objective saturation then forces every row to one of the two displayed modes. The first and third column sums give the subset weight and cardinality. The complete current argument, including legal boundary inputs and polynomial encoding, is [proof.md](../../work/proof.md); both executable maps are [algorithm.py](../../work/algorithm.py).

Local enumeration: 36 (k,a) pairs and 6076 feasible configurations, all matching the two-maximizer claim ([output](local-output.jsonl)). Prepared injection: eight inputs, four YES/four NO, eight recovery calls. Additional verification: 327 inputs, 94 YES/233 NO, 848 solver queries and all 521 target witnesses recovered. See [verification report](../../work/verification.md) for actual targets, commands, all-witness coverage and the independent bound-cut audit.

Repairs and reruns: the construction formula was unchanged. Added explicit malformed-input outputs and disabled Python's decimal digit ceiling before final checks; preserved and repeated the prepared run. The first additional verification run completed 326 inputs, 847 completed solver queries and 521 recovery calls; its final NO query was interrupted while replacing the oracle with proved redundant objective bounds. Z3 returned unknown and the checker raised. That pending query is one interrupted query, not a NO. The changed checker reran the whole declared scope successfully. These runs do not constitute new discovery rounds or additional unique coverage. No timeout or hidden retry. The subsequent independent review is linked below. Time/token totals unavailable.

Novelty check, 2026-09-16: revisited Koutecký and Zink, [2025 journal article](https://link.springer.com/article/10.1007/s10951-024-00827-8), Theorem 4.14, the following open-question paragraph, and Section 5.2; also the [arXiv record](https://arxiv.org/abs/2009.11840). Their four-type hardness construction is not this three-type rule. Queries: `"unrelated" "three job types" scheduling NP-hard`; `"scheduling" "3 job types" "hard"`; `"high-multiplicity" "scheduling" "three" 2026`; `"scheduling" "two configurations" "partition" hardness`; `unrelated machines high multiplicity three types jobs NP hardness 2026`; `"2009.11840" three types`; `"high-multiplicity" "3" "NP-hard" scheduling`. No matching resolution was located. Sun's [2026 rejection-scheduling paper](https://link.springer.com/article/10.1007/s10878-026-01455-y), abstract, concerns rejection and an exact algorithm with polynomially bounded total jobs. Its full subscription text was not audited. This is an explicit coverage gap, not confirmation of novelty. The 2001 paper discussed in round 4 does not state three-type hardness.

Significance: lowering the fixed-type hardness boundary from four to three is a concrete scheduling-complexity contribution. This proof supplies ordinary NP-completeness, not strong hardness, approximation hardness, or a new two-type algorithm. Correctness, novelty and significance remain separate review judgments.

Experience extraction: pending new entry `research/experience/common-objective-scheduling-selectors.md`. Premises: the exact family above, positive source weights, k>=max a_i, compact integer encoding. Finding: nonnegative perturbations of a shared integer objective can expose input-dependent pairs while a global count identity forces every machine onto the exposed pair; product rescaling supplies a common deadline without exponential bit length. Evidence: the complete proof and actual forward/recovery checks. This uses round 7's extra directions and avoids round 8's midpoint obstruction. The candidate received an independent advance review, linked below. Shared destination remains outside the write boundary.

## Next action

Stop discovery at round 9 and request the required native independent reviewer. If review advances, write and inspect the Typst paper without charging extra rounds. There is no reason to manufacture fourteen further attempts once a complete rule exists. A substantive repair would start another round within the remaining allocation.

## Review and writing closure

The [native independent review](../../reviews/affine-selector/review.md) advances the unchanged rule. It supplies its own exact checks and a separate literature/bit-bound audit; it does not certify publication acceptance. The [five-page English manuscript](../../work/manuscript.pdf), [Typst source](../../work/manuscript.typ), and [page inspection](../../work/evidence/manuscript/inspection.md) complete writing. Status: ready_for_expert_review. Discovery used rounds 4–9 of this additional allocation; rounds 10–23 remain unused because the full rule completed the pipeline. No shared experience files were written: five distinct proposed entries remain recorded locally under the campaign-only boundary.

## Shared experience consolidation — 2026-09-16

After explicit user authorization, the finding and its recorded qualifications
were saved in [Common-objective scheduling selectors](../../../../research/experience/common-objective-scheduling-selectors.md).
The pending status above describes the original round closure and is now
resolved. The use history distinguishes round-level findings from later shared
publication; no research tests were rerun for this documentation transfer.
