# Round 5: Exact-load divisibility

## Plan

Replace interval capacity by saturated arithmetic loads. Start with the published (6,10,15) example from round 4. For pairwise-coprime integers p,q,r>1, use processing times (qr,pr,pq) and capacity pqr. Classify all full-load configurations by reducing the load equation modulo p,q,r. Test the published infeasible instance and all full-load configurations for pairwise-coprime triples 2<=p<q<r<=11. Completion: determine whether arbitrary item-dependent binary choices arise. This is one generalization/diagnosis, not a complete source map.

## Evidence and diagnosis

For a full configuration, qr x+pr y+pq z=pqr. Modulo p, coprimality forces p|x; similarly q|y and r|z. Division gives x/p+y/q+z/r=1. Hence the only full configurations are (p,0,0),(0,q,0),(0,0,r). This is a general elementary argument, not an inference from enumeration.

If the global workload equals the total capacity of m identical machines, every row must be full. Feasibility in this family is exactly divisibility of the three job counts by p,q,r together with their quotients summing to m. The published instance has total load 59, not 60, so saturation alone does not prove its infeasibility. The one exact solver call separately confirms that published NO instance. This distinction prevents an incorrect reuse of the saturation lemma.

[Probe](probe.py) and [raw output](output.jsonl): 42 coprime triples checked by exact enumeration and one Z3 query (UNSAT). No candidate source map, recovery call, repair or rerun. Reproduce: `python3 campaigns/three-type-unrelated-scheduling/rounds/005/probe.py`. Time/token totals unavailable.

Experience extraction: pending new finding `research/experience/saturated-coprime-scheduling.md`. Premises: identical rows (qr,pr,pq), pairwise-coprime p,q,r, and saturated total load. Consequence: pure-type local modes alone yield a divisibility algorithm, not weighted subset selection. Evidence: the modular proof and 42 finite checks here. Main-agent checked; novelty unassessed. Shared destination is outside the authorized campaign write boundary.

## Next action

Allow machine-dependent capacities with common job lengths, preserving saturation by a global workload identity. Inspect the integer solution fibers of three-generator numerical semigroups: can two-point fibers have sufficiently many different displacement vectors to encode input weights? This changes the identical-capacity premise and is not coefficient tuning within the excluded family.

## Shared experience consolidation — 2026-09-16

After explicit user authorization, the finding and its recorded qualifications
were saved in [Saturated coprime scheduling](../../../../research/experience/saturated-coprime-scheduling.md).
The pending status above describes the original round closure and is now
resolved. The use history distinguishes round-level findings from later shared
publication; no research tests were rerun for this documentation transfer.
