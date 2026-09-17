# Fixed-fill binary scheduling selectors admit an interval algorithm

Tags: scheduling, fixed-fill, binary-selector, integer-interval, tractable-subclass

## Claim and applicability

Assume each machine i has a known nonnegative fixed total b_i of types one
and two, and a third-type count z_i in {0,1}. Global counts are
(X,sum_i b_i-X,K), with positive processing times and a common threshold T.
This restricted allocation model has a deterministic polynomial algorithm.

Writing x_i for the first-type count gives

\[
0\le x_i\le b_i,\qquad
(p_{i1}-p_{i2})x_i\le T-p_{i2}b_i-p_{i3}z_i.
\]

At fixed z_i, the allowed integers form an interval. Changing z_i from zero
to one only increases its lower endpoint or decreases its upper endpoint,
according to the coefficient sign. Discard impossible selections. Group
remaining machines by the affected endpoint, sort their endpoint losses,
and try each split of K selections between the groups. The smallest losses
minimize both penalties for that split. Test whether the sum interval
contains X, then fill it greedily. Reject K>m before iterating.

This does not solve unrestricted three-type scheduling. Applying the result
to a reduction requires proving its fixed-fill and binary premises and
computing the b_i in polynomial time.

## Evidence and status

[Round 2](../../campaigns/three-type-unrelated-scheduling/rounds/002/round.md) contains the general argument and
implementation: 192 exact comparisons with Z3 and a separate large-K
boundary check. The direct algorithm uses O(m^2) arithmetic operations on
polynomial-bit integers. Main-researcher checked; no independent review or
novelty claim for this restricted-model lemma.

## Consequence for search

A hardness construction contained in this explicitly known restricted model
would imply P=NP. Change a structural premise before further synthesis.
Do not infer hardness merely from large binary coefficients.

## Use history

[Round 3](../../campaigns/three-type-unrelated-scheduling/rounds/003/round.md) allowed nonbinary third counts to leave
this model; its failure had a different partial-fill explanation. The
[successful round 9](../../campaigns/three-type-unrelated-scheduling/rounds/009/round.md) has variable fill totals and
potentially nonbinary third counts, so this obstruction does not apply.
This is a premise comparison, not a controlled measurement of discovery benefit.

Consolidated on 2026-09-16 after user authorization; the original round
findings preceded this shared file.
