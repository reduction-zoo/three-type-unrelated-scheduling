# Round 2 — Fixed fill counts and binary selectors

## Plan

Analyze the restricted allocation model where each machine i has a known
fixed total b_i of types one and two, and its type-three count z_i is binary.
The global totals are X, sum b_i-X, and K. Processing times and T remain
arbitrary positive integers. This abstracts a broad proposed selector route,
not the whole target language. For each z_i, the feasible type-one counts form
an integer interval; choosing z_i=1 only shrinks one endpoint. Determine whether
selecting K such intervals can be done by sorting the endpoint losses. If so,
a Karp construction whose soundness imposes these premises cannot establish
hardness unless P=NP. Check the proposed deterministic interval algorithm
against exact Z3 on 192 seeded instances: 2–6 machines, b_i in 1–4,
processing times in 1–9, T in 0–40, legal global counts; seed 20260916.
Use the pending one-sided-capacity finding from round 1. The new question is
a general tractability boundary, not another coefficient tweak.

## General argument

Write x_i for the first-type count, so the second count is b_i-x_i. At fixed
z_i, feasibility is

\[
0\le x_i\le b_i,\qquad
(p_{i1}-p_{i2})x_i\le T-p_{i2}b_i-p_{i3}z_i.
\]

Thus the allowed integer values form an interval I_i(z_i). If I_i(0) is empty,
no solution exists. A machine with empty I_i(1) cannot be selected. Otherwise
I_i(1) is contained in I_i(0). When the slope is positive, only the upper
endpoint decreases; when negative, only the lower endpoint increases. A zero
slope either excludes selection or leaves the interval unchanged.

Partition eligible machines into lower-endpoint and upper-endpoint losses,
putting unchanged intervals in the latter group with loss zero. For each h,
select the h smallest lower losses and K-h smallest upper losses. This choice
minimizes both endpoint penalties among selections with those group counts.
The sum of integer intervals contains every integer between the endpoint sums,
so it contains X precisely when the resulting total lower bound is at most X
and total upper bound is at least X. Try every feasible h and fill intervals
greedily to construct a witness. Reject K>m before iteration. Sorting and the
direct implementation take O(m^2) arithmetic operations on polynomial-bit
integers; the witness is an m-by-three count matrix.

This proves tractability of the stated restricted model. It does not prove
tractability of three-type scheduling with arbitrary machine job counts.
A hardness construction that establishes known b_i and binary selectors for
all its schedules would also have to evade this algorithm; otherwise composing
it with the algorithm would decide the source in polynomial time.

## Evidence and diagnosis

[Output](output.jsonl): 192 exact comparisons against Z3 under the same added
restrictions, with directly checked constructed witnesses. The algorithm agrees
in every case. A code-inspection correction added immediate rejection of K>m
to avoid iterating over a large binary count; a [separate boundary check](count-bound-check.txt)
passes. The original 192 cases have K<=m and were not rerun. One boundary
correction, no failed execution, no repeated solver calls. This is a main-agent
argument and implementation, not independent review or a novelty claim.
Time/token totals unavailable.

Experience extraction: pending `research/experience/fixed-fill-binary-scheduling-selector.md`.
Claim and scope: the interval algorithm above. Evidence: general argument,
192 exact comparisons, and the large-count boundary check. Consequence:
leave either fixed filler totals or binary selector counts before searching for
hardness by this mechanism. Shared destination remains blocked by campaign scope.

## Next action

Allow many selector jobs and test a modular completion-bonus mechanism.
Reproduce with `python3 campaigns/three-type-unrelated-scheduling/rounds/002/probe.py`.

## Shared experience consolidation — 2026-09-16

After explicit user authorization, the finding and its recorded qualifications
were saved in [Fixed-fill binary selectors](../../../../research/experience/fixed-fill-binary-scheduling-selector.md).
The pending status above describes the original round closure and is now
resolved. The use history distinguishes round-level findings from later shared
publication; no research tests were rerun for this documentation transfer.
