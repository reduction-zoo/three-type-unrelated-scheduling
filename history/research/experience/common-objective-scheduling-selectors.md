# Common-objective saturation forces input-dependent scheduling choices

Tags: scheduling, Karp-reduction, balanced-partition, exposed-configurations, saturation, witness-recovery, binary-encoding

## Claim and applicability

Suppose each machine has a proved integer objective bound w.x_i<=b_i,
with the same positive vector w. If prescribed global counts satisfy
w.n=sum_i b_i, every feasible schedule attains every local bound. Proving
that precisely two configurations attain each bound therefore forces a
binary choice without adding an objective to the target decision problem.

A concrete three-type realization uses positive source weights a_i,
k=max_i a_i, H=4(k+1)^2, and w=(k,k+1,2k+1). Set

\[
b_i=(k+1)(2k+1-a_i),\quad s_i=a_i(2k+1-a_i),
\]
\[
p_i=Hw+(2k+1-a_i,a_i,0),\qquad C_i=Hb_i+s_i.
\]

The only feasible configurations attaining b_i are
u_i=(0,2k+1-a_i,0) and v_i=(a_i,0,k+1-a_i).
For nonempty even-length sources with even total A, global counts
(A/2,m(2k+1)/2-A/2,m(k+1)/2-A/2) saturate the objective bounds.
The first column recovers selected weight; the third recovers cardinality.
Every valid target witness therefore yields a balanced subset by its v_i rows.
Empty and odd-total cases have explicit legal outputs in the implementation.

Normalize local capacities to one deadline using T=product_i C_i and
P_i=(T/C_i)p_i. This preserves every row's feasible set. Its bit length is
O(m log(k+1)); multiplication of capacities does not require expanding jobs.
The argument depends on exact integer data and proved bounds. Merely finding
two preferred solver outputs does not establish the selector property.

## Evidence and status

The [general proof](../../campaigns/three-type-unrelated-scheduling/work/proof.md), [two executable maps](../../campaigns/three-type-unrelated-scheduling/work/algorithm.py),
and [round 9](../../campaigns/three-type-unrelated-scheduling/rounds/009/round.md) establish the construction and polynomial
bounds. [Verification](../../campaigns/three-type-unrelated-scheduling/work/verification.md) checks 327 inputs and all
521 target witnesses for them. The [independent review](../../campaigns/three-type-unrelated-scheduling/reviews/affine-selector/review.md)
advances the unchanged rule after its own checks and literature audit.
Human expert assessment remains outstanding. Novelty is supported only within
the recorded search coverage; no strong-hardness or approximation claim follows.

## Consequence for search

Look for a shared auxiliary invariant whose total is fixed by target counts,
then expose locally useful configurations with a nonnegative perturbation.
Prove the maximum and classify all maximizers before composing the machines.
Check source weight and cardinality separately in recovery, and assess products
by binary length rather than numerical magnitude.

## Use history

No subsequent campaign use is recorded. This construction developed from
rounds [7](../../campaigns/three-type-unrelated-scheduling/rounds/007/round.md) and [8](../../campaigns/three-type-unrelated-scheduling/rounds/008/round.md);
that discovery history is not later reuse of this entry.

Consolidated on 2026-09-16 after user authorization. The independent review
concerns the linked candidate proof, not an independent audit of this summary.
