# One-sided partition capacity permits false positives

Tags: scheduling, balanced-partition, blockers, partial-fill, soundness, counterexample

## Claim and applicability

For a nonempty even-length list of positive weights with even total A, the
full-blocker construction with H=A^3, T=AH, processing rows
(H+A-a_i,H-a_i,T), and counts (A/2,(m-1)A/2,m/2) is always feasible.
Its unblocked machines need only have total weight at least A/2. Choosing
the largest half and filling their first-type capacities greedily supplies
a schedule, even when the source has no balanced partition.

A separate modular construction also permits partial-fill bypass. With
T=(A+1)^4 product_i a_i, rows (T/a_i-a_i-1,T/a_i,a_i), and counts
(A/2,A/2,A/2+m/2), the first two counts on machine i sum to a_i and its
third count satisfies z_i<=x_i+floor(x_i/a_i). Complete the smallest half
of the items and use partial first-type fills elsewhere. This always meets
the required counts. These claims concern the two displayed families,
not all blockers or modular reductions.

## Evidence and status

General counter-constructions in [round 1](../../campaigns/three-type-unrelated-scheduling/rounds/001/round.md) and
[round 3](../../campaigns/three-type-unrelated-scheduling/rounds/003/round.md), each with 24 checked target witnesses,
including twelve source-NO cases. Main-researcher arguments; these diagnostic
lemmas have not received independent review. No novelty claim.

## Consequence for search

Before tuning coefficients, derive what each global count actually forces.
An inequality on the selected weight needs a second constraint establishing
equality. A completion bonus does not enforce indivisible item selection
when partial fills can absorb the remaining count.

## Use history

- [Round 2](../../campaigns/three-type-unrelated-scheduling/rounds/002/round.md) used the missing-bound diagnosis to
  analyze a larger fixed-fill family instead of retuning the same blocker.
- [Round 3](../../campaigns/three-type-unrelated-scheduling/rounds/003/round.md) changed the binary-selector premise,
  but the explicit partial-fill construction exposed the same missing bound.

Consolidated on 2026-09-16 after user authorization. These uses refer to the
findings recorded in the original rounds, before this shared entry existed.
