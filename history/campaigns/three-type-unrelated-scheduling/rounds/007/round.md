# Round 7: Common objective on unrelated knapsacks

## Plan

For positive objective w shared by all machines, let b_i=max{w.x: p_i.x<=T, x>=0 integer}. If global counts n satisfy w.n=sum b_i, all rows of every feasible schedule maximize w.x. Search for knapsacks with exactly two maximizing configurations and different displacements under one w. Unlike round 6, the feasible slice may discard configurations with the same objective. Composition obligation: choose polynomially describable p_i and a common T for input-dependent choices, and recover each selection from any schedule. This round tests only direction diversity, a necessary interface property.

Finite scope: four objectives (1,1,1),(2,3,5),(5,7,11),(6,10,15); processing vectors in {1,...,12}^3; capacity 1..60. Enumerate exact configurations, retain maximum objective at each capacity, and count displacement directions when exactly two maximizers exist. Stop after the declared finite domain; no synthesis claim outside it. Local varying capacities can be normalized to a common deadline using a common multiple and integer rescaling, with polynomial bit length for an explicit list.

## Evidence and diagnosis

The changed premise matters. For shared objective (2,3,5), unrelated local knapsacks realize seven different two-maximizer directions in the declared range; the three-direction conclusion of round 6 does not extend to this model. [Raw output](output.jsonl) saves one exact example per direction. The four objectives give direction counts [3, 7, 6, 3], respectively. There are 15451 two-maximizer cases among 4*12^3*60=414720 objective/knapsack/capacity checks. The [probe](probe.py) enumerates all feasible configurations, not selected solver models. Zero Z3 queries, source maps, recovery calls, repairs or reruns. Reproduce: `python3 campaigns/three-type-unrelated-scheduling/rounds/007/probe.py`. Time/token totals unavailable.

If capacity C_i varies locally, take T=product C_i and replace processing row p_i by (T/C_i)p_i. Feasibility is unchanged, and log T=sum log C_i. Thus normalization is polynomial in an explicitly supplied gadget list. If w.n=sum b_i, summing local objective bounds forces equality on every machine. These two facts justify composition prerequisites but do not construct n or encode source weights. Seven fixed directions still permit enumeration of selection counts in polynomial time. A scalable input-dependent set of directions is required.

Experience extraction: update the pending round-6 finding with this counterexample to extending its premises. Destination `research/experience/three-length-two-configuration-fibers.md` remains pending. The distinction between complete fibers and two maximizers after unrelated cuts is supported by exact enumeration, not by a completed reduction.

## Next action

Try an explicit growing family: w=(1,Q,R), modes (0,0,1) and (R-Qa_i,a_i,0). Their displacement is affine in the source weight, so global counts can express both subset cardinality and sum. Before synthesis, check whether a positive processing row can retain precisely these two maximizers for interior a_i.

## Shared experience consolidation — 2026-09-16

After explicit user authorization, the finding and its recorded qualifications
were saved in [Two-configuration fibers and separation limits](../../../../research/experience/three-length-two-configuration-fibers.md).
The pending status above describes the original round closure and is now
resolved. The use history distinguishes round-level findings from later shared
publication; no research tests were rerun for this documentation transfer.
