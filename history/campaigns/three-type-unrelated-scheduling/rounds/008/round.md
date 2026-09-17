# Round 8: Affine-weight exposed selectors

## Plan

Use shared objective w=(1,Q,R), with Q>0 and R>Q max(a_i), and intended local modes u=(0,0,1), v_i=(R-Qa_i,a_i,0). Their displacement (R-Qa_i,a_i,-1) would encode balanced cardinality and sum through the three global column counts. Look for one positive processing inequality retaining these two as the only objective maximizers. Scope: general interior case 1<=a_i and Q(a_i+1)<=R; inspect adjacent integer configurations and prove or refute separability. One symbolic template, no coefficient search unless the local separation test passes. Completion: resolve this necessary local property before constructing a full map.

## Evidence and diagnosis

The intended v_i is the midpoint of two distinct nonnegative integer configurations v_minus=(R-Q(a_i-1),a_i-1,0) and v_plus=(R-Q(a_i+1),a_i+1,0). Both have objective R. For every linear processing row, their costs average to the cost of v_i. If v_i fits, at least one of them fits too. Thus u and v_i cannot be the only maximizers. This is a general separation obstruction for the stated interior range; no finite solver search is needed. Adding a common nonnegative translation to all three configurations does not remove it.

Actual work: one symbolic template refuted; zero queries, source instances, recovery calls, repairs or reruns. Time/token totals unavailable. Experience extraction: pending addition to `research/experience/three-length-two-configuration-fibers.md` from round 6: a retained configuration that is an integer midpoint cannot be isolated with a single linear capacity inequality from both neighbors. Exact premises and proof are here; no general impossibility for all affine displacement families is claimed.

## Next action

Round 7 contains a different affine family for w=(2,3,5): displacements (a,a-5,3-a). Unlike the failed template, the two endpoint configurations move on different coordinate faces as a changes. Test the generalization w=(k,k+1,2k+1), d(a)=(a,a-(2k+1),k+1-a), with k>=max a_i. Its nonnegative endpoint configurations are u=(0,2k+1-a,0) and v=(a,0,k+1-a). Inspect the entire objective fiber before constructing the reduction.

## Shared experience consolidation — 2026-09-16

After explicit user authorization, the finding and its recorded qualifications
were saved in [Two-configuration fibers and separation limits](../../../../research/experience/three-length-two-configuration-fibers.md).
The pending status above describes the original round closure and is now
resolved. The use history distinguishes round-level findings from later shared
publication; no research tests were rerun for this documentation transfer.
