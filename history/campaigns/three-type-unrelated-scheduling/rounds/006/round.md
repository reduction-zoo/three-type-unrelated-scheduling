# Round 6: Two-configuration fibers

## Plan

Investigate saturated common-length machines with varying capacities C_i. For common positive lengths l=(l1,l2,l3), the full configurations are F(C_i)={x>=0 integer: l.x=C_i}. A two-point fiber would provide a true atomic choice; distinct displacement vectors would be needed to encode many input weights. Search primary numerical-semigroup literature for bounds on two-point fibers / minimal relations in three generators. Finite diagnostic: strictly increasing lengths 2..12 with gcd 1, capacities 1..240; count distinct differences for fibers of exactly two points, oriented lexicographically. One family, all declared tuples, no source candidate. Completion: find a scalable selector or a precise obstruction to this two-point-fiber route.

## Evidence and diagnosis

There are at most three different displacement vectors (up to sign) among all two-point fibers of any fixed three positive lengths. Here is a direct proof, independent of the literature lead. Given the two configurations u,v, subtract their coordinatewise minimum h. The residual fiber has exactly two configurations: any third would remain a third after adding h. Their supports are disjoint, so one is c e_j for some coordinate j. If a smaller positive multiple c' l_j were representable using the other two lengths, that representation plus (c-c')e_j would be a third residual configuration. Thus c is the least such multiple. Its representation using the other lengths must be unique. For each j, this determines at most one displacement. There are three coordinates. The argument also allows redundant generators and nonunit gcd.

Consequently, when each machine's complete full-load fiber consists of two explicitly supplied configurations, choose a lexicographic base per machine and group its displacement by these at most three vectors. Enumerate how many machines take the second configuration in each group (at most (m+1)^3 triples), then check the global count vector. Choosing arbitrary machines within each group reconstructs a schedule. This is polynomial in the supplied configurations' binary encoding; no claim is made here about an algorithm to enumerate fibers from binary lengths. A reduction that explicitly supplies its two intended full configurations and proves they are the only ones would supply exactly this information. Therefore this particular atomic-choice route is tractable unless P=NP.

[Probe](probe.py) and [output](output.jsonl) cover 141 length triples, 33840 positive-capacity fibers, and 1189 two-point fibers. At most 3 directions occurred per length triple. Zero Z3 queries, source instances, recovery calls, repairs or reruns. Reproduce: `python3 campaigns/three-type-unrelated-scheduling/rounds/006/probe.py`. Time/token totals unavailable.

Literature search on 2026-09-16: `three generated numerical semigroup minimal presentation at most three relations Betti elements two factorizations`. The [NumericalSgps documentation](https://gap-packages.github.io/numericalsgps/doc/chap4.html), Section 4.1, identifies presentations as generating trades between factorizations. No external three-relation bound is used in the proof above, and the broader presentation literature was not audited.

Experience extraction: pending new finding `research/experience/three-length-two-configuration-fibers.md`. Exact premises and algorithm are above. Evidence: direct proof and finite enumeration; main-agent checked, novelty unassessed. This excludes a narrower construction family, not three-type unrelated scheduling. Shared writing is blocked by the campaign-only instruction.

## Next action

Change common processing lengths to a common positive auxiliary objective, allowing unrelated processing vectors. If each machine has exactly two maximizers and the global objective is saturated, those maximizers become forced. Test whether this permits more than three displacement directions. This is a necessary local-interface test, not a claimed source reduction.

## Shared experience consolidation — 2026-09-16

After explicit user authorization, the finding and its recorded qualifications
were saved in [Two-configuration fibers and separation limits](../../../../research/experience/three-length-two-configuration-fibers.md).
The pending status above describes the original round closure and is now
resolved. The use history distinguishes round-level findings from later shared
publication; no research tests were rerun for this documentation transfer.
