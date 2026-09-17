# Round 1 — Complete blockers and one-sided partition constraints

## Plan

Replace the failed partial blocker by a job of length T on every machine.
For source items a_i, even total A, and even item count m, let H=A^3, T=AH.
Use processing times (H+A-a_i,H-a_i,T) and multiplicities
(A/2,(m-1)A/2,m/2). A blocker selects half the machines and excludes every
other job there. The other machines must each receive A jobs. Test whether
this fixes the source converse or enforces only one side of the partition
condition. Scope: derive the feasible-schedule condition and construct or
reject schedules for the 24 existing screening sources, without re-solving
their source predicates. This is a changed blocker and multiplicity mechanism,
not a repeat of the merger. No complete extractor is proposed until soundness
survives. Experience search found no applicable scheduling entry; the existing
false positive is the regression motivating the change.

## Evidence and diagnosis

The construction is YES for every positive even-length source with even total.
A blocker fills its machine completely. There are m/2 unblocked machines and
mA/2 other jobs. Since (A+1)(A^3-a_i)>A^4 for A>=2 and a_i<=A-1,
each unblocked machine receives exactly A jobs. If it receives x_i jobs of
type one, its capacity condition reduces to x_i<=a_i. Thus the only condition
on the unblocked set S is sum_{i in S} a_i>=A/2. The largest m/2 entries always
satisfy it. Allocate the A/2 type-one jobs greedily under these capacities and
fill each selected machine to A jobs with type two.

[Output](output.jsonl) validates 24 explicit schedules, including all twelve
NO sources. No target solver calls were needed: these constructive witnesses
and the general argument suffice. The deterministic counter-construction uses
O(m log m) comparisons and polynomial-bit arithmetic. It diagnoses this family;
it is not the desired source-to-target reduction. No repairs/reruns, independent
review or novelty claim; time/token totals unavailable.

Experience extraction: pending `research/experience/one-sided-partition-capacity.md`.
Claim: the displayed full-blocker construction enforces only a lower bound on
the selected sum and is always YES. Applicability and exclusions are the exact
processing-time and multiplicity formulas above. Consequence: a repaired route
must supply the missing opposite bound. Evidence is a general argument and
24 witnesses. Shared writes are blocked by the campaign-only instruction.

## Next action

Assess the broader fixed-fill, binary-selector family before tuning coefficients.
Reproduce with `python3 campaigns/three-type-unrelated-scheduling/rounds/001/probe.py`.

## Use in round 3

[Round 3](../003/round.md) changed to nonbinary selectors and a modular
completion bonus. The same missing-bound diagnosis appeared through partial
fills. The pending finding now covers the two explicit constructions, with
separate proofs; it does not exclude every arithmetic three-type reduction.

## Shared experience consolidation — 2026-09-16

After explicit user authorization, the finding and its recorded qualifications
were saved in [One-sided partition capacity](../../../../research/experience/one-sided-partition-capacity.md).
The pending status above describes the original round closure and is now
resolved. The use history distinguishes round-level findings from later shared
publication; no research tests were rerun for this documentation transfer.
