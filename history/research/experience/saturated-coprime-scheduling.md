# Saturated coprime scheduling reduces to divisibility

Tags: scheduling, coprime, exact-load, saturation, modular-arithmetic, pure-configurations

## Claim and applicability

Let p,q,r>1 be pairwise coprime. Give every machine processing times
(qr,pr,pq) and capacity pqr. Assume the prescribed total workload equals
m times this capacity. Every machine must then be full, and its only
possible configurations are (p,0,0), (0,q,0), and (0,0,r).

Indeed, reducing qr x+pr y+pq z=pqr modulo p,q,r forces p|x, q|y and r|z.
The nonnegative integers x/p,y/q,z/r sum to one. Global feasibility is
therefore exactly divisibility of the three counts by p,q,r and the
condition that their quotients sum to m.

Both identical processing rows and total-load saturation are premises.
The statement does not classify instances with idle capacity, varying
processing rows, or additional eligibility restrictions.

## Evidence and status

[Round 5](../../campaigns/three-type-unrelated-scheduling/rounds/005/round.md) gives the modular proof and exhaustive
checks for 42 coprime triples with 2<=p<q<r<=11. Main-researcher checked;
no independent review or novelty claim.

The separate published two-machine example with lengths (6,10,15), counts
(4,2,1), and capacity 30 has total load 59, not 60. Its recorded UNSAT
check is not an application of the saturated lemma. The primary-source
location is recorded in [round 4](../../campaigns/three-type-unrelated-scheduling/rounds/004/round.md).

## Consequence for search

Pure-type local choices do not alone implement weighted subset selection.
In this family they yield only a direct divisibility test. A candidate must
explain how input-dependent choices couple globally beyond these divisibilities.

## Use history

[Round 6](../../campaigns/three-type-unrelated-scheduling/rounds/006/round.md) changed to varying local capacities with
common processing lengths, investigating whether their exact-load fibers
could encode different item choices. Its own obstruction had different premises.

Consolidated on 2026-09-16 after user authorization; the round-level use
preceded this shared entry.
