# Three-type unrelated-machine scheduling

Status: **ready_for_expert_review**. Budget: **9/23 rounds completed** (six of the
20 newly authorized rounds used). Fourteen discovery rounds remain unused.
Fixed target: [question](question.md).

## Current result

[Algorithm](work/algorithm.py) and [general proof](work/proof.md) give a candidate
Karp reduction from Balanced Partition to three-type unrelated-machine makespan
feasibility, with recovery from every valid target count matrix. The candidate
uses a shared auxiliary objective to force two input-dependent configurations
on each machine. It emits a single common deadline with polynomial binary size.
No known proof gap or test mismatch remains; expert validation is outstanding.

[Verification](work/verification.md) passes 327 inputs (94 YES/233 NO), all
521 target witnesses and their recoveries, plus the eight prepared inputs.
A large-query interruption and the mathematically equivalent oracle improvement
are recorded explicitly. No timeout was used. The original 326 completed
checks remain preserved; repeated cases do not enlarge unique coverage.

Novelty is supported within documented primary-source search coverage, not
proved by search absence. Importance is moderate: improve the known fixed-type
hardness boundary from four to three. No strong hardness or approximation gap
is claimed. The [native independent reviewer](reviews/affine-selector/review.md) gave
**advance** on correctness, novelty within documented coverage, and significance.
Its own checks and literature audit are saved in that directory. The candidate
and proof were not changed after review. The [English paper](work/manuscript.pdf)
and [Typst source](work/manuscript.typ) are complete; all five pages were
[visually inspected](work/evidence/manuscript/inspection.md). Next: expert human
assessment. No additional discovery round is needed to fill the unused budget.

## Rounds

| Round | Result |
|---|---|
| [1](rounds/001/round.md) | Full blockers: always-YES counter-construction, 24 witnesses |
| [2](rounds/002/round.md) | Fixed-fill binary selectors: polynomial interval algorithm, 192 comparisons |
| [3](rounds/003/round.md) | Modular bonuses: partial-fill bypass, 24 witnesses |
| [4](rounds/004/round.md) | Literature: three-type integer-allocation obstruction |
| [5](rounds/005/round.md) | Saturated coprime rows: divisibility only; 42 triples, one published NO checked |
| [6](rounds/006/round.md) | Complete two-point fibers: at most three directions; 141 length triples |
| [7](rounds/007/round.md) | Unrelated cuts: seven directions under one objective; 414720 finite local checks |
| [8](rounds/008/round.md) | First affine selector excluded by an integer-midpoint argument |
| [9](rounds/009/round.md) | Scalable affine selector, full rule and general proof; independent advance and inspected paper |

Rounds measure attempts, including literature and diagnosis; they are not nine
independent successful constructions. Round 9's local enumeration checks 36
parameter pairs and 6076 configurations. Full verification makes 848 exact Z3
queries and 521 recovery calls; earlier and repeated runs are listed separately
in its record. Aggregate time/token measurements are unavailable.

## Experience extraction

On 2026-09-16, the user explicitly authorized saving all five findings to the
shared experience library. **5 shared entries created, 0 existing entries
updated, 0 pending.** This supersedes the earlier campaign-only deferral.

- [One-sided partition capacity](../../research/experience/one-sided-partition-capacity.md).
- [Fixed-fill binary selectors](../../research/experience/fixed-fill-binary-scheduling-selector.md).
- [Saturated coprime scheduling](../../research/experience/saturated-coprime-scheduling.md).
- [Two-configuration fibers and separation limits](../../research/experience/three-length-two-configuration-fibers.md).
- [Common-objective scheduling selectors](../../research/experience/common-objective-scheduling-selectors.md).

Each English entry records exact premises, exclusions, evidence links, review
status and use history. Consolidation is retrospective; no earlier shared-file
retrieval or measured discovery improvement is claimed. Original evidence and
round histories remain in this campaign. The mathematical rule, tests, review,
manuscript, board and production repository were not changed by this transfer.
