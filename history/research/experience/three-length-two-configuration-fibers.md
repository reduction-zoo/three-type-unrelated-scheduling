# Two-configuration fibers: direction bounds and separation limits

Tags: scheduling, numerical-semigroup, two-point-fiber, displacement, midpoint, unrelated-machines

## Claim and applicability

For any fixed three positive lengths l, consider the complete fibers
F(C)={x in Z_{≥0}^3: l.x=C}. Among fibers containing exactly two points,
there are at most three distinct displacement vectors, up to sign.

Subtract the coordinatewise minimum of the two points. Their residual
supports are disjoint, so one point is c e_j. A smaller positive multiple
of l_j representable using the other lengths would give a third residual
point. Thus c is the least such multiple and its alternative representation
must be unique. Each of the three coordinates determines at most one displacement.

When a saturated common-length construction explicitly supplies the two
complete configurations on every machine, group their oriented displacements
and enumerate the selected count in each group. At most (m+1)^3 group-count
triples suffice. This is polynomial in the supplied configurations; it does
not assert that all fibers can be enumerated efficiently from binary lengths.

The word **complete** matters. Unrelated capacity cuts can retain two
maximizers from a larger common-objective fiber and escape this direction
bound. However, a retained point that is the midpoint of two distinct integer
points of the same objective cannot be isolated from both by one linear
capacity inequality: at least one neighbor has no greater processing cost.

## Evidence and status

[Round 6](../../campaigns/three-type-unrelated-scheduling/rounds/006/round.md) proves the direction bound and checks
141 length triples, 33840 capacities and 1189 two-point fibers.
[Round 7](../../campaigns/three-type-unrelated-scheduling/rounds/007/round.md) finds seven directions for the shared
objective (2,3,5) after unrelated cuts, refuting extension to that model.
[Round 8](../../campaigns/three-type-unrelated-scheduling/rounds/008/round.md) gives the midpoint argument for its
explicit affine selector. These diagnostic arguments are main-researcher
checked, not independently reviewed; no novelty claim.

## Consequence for search

Distinguish a complete equality fiber from the points surviving a second
inequality. Check integer midpoint obstructions before coefficient synthesis.
Neither result excludes all input-dependent affine selectors.

## Use history

Rounds [7](../../campaigns/three-type-unrelated-scheduling/rounds/007/round.md) and [8](../../campaigns/three-type-unrelated-scheduling/rounds/008/round.md)
tested the changed premise and its local separation requirements.
[Round 9](../../campaigns/three-type-unrelated-scheduling/rounds/009/round.md) generalized actual round-7 directions
using endpoints on different coordinate faces, avoiding the round-8 obstruction.
The resulting reduction passed independent review, but this history does not
measure the causal benefit of experience retrieval.

Consolidated on 2026-09-16 after user authorization; these uses concern the
precursor findings, not a shared file that existed during discovery.
