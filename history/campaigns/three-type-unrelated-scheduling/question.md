---
status: proof-route-hold
openness: supported-within-search-coverage
difficulty: uncertain
importance: moderate
tags: [scheduling, high-multiplicity, unrelated-machines, three-job-types, NP-hardness]
last-literature-check: 2026-09-16
---

# Balanced Partition to three-type unrelated-machine scheduling

[Board](README.md) · [Karp contract](README.md#shared-karp-contract)

**Decision: next screening priority, not an admitted campaign.** No complete
three-type construction has been found. A tested direct type merger fails.

## Fixed target

The source is Balanced Partition: an even-length list of positive binary integers
asks for a subset containing half the entries and half their total sum.
The target gives an explicit list of m unrelated machines, at most three job
types, positive integer processing times p_ij, binary multiplicities n_j, and
an integer makespan threshold T. All jobs are independent and nonpreemptive.
The predicate is the existence of nonnegative integer counts x_ij such that

\[
\sum_i x_{ij}=n_j\quad\text{for each type }j,\qquad
\sum_j p_{ij}x_{ij}\le T\quad\text{for each machine }i.
\]

Seek a deterministic polynomial-time Karp reduction, with polynomial output
bit length, and recovery of a balanced source subset from every feasible count
matrix. All well-formed source instances must produce legal target instances;
malformed strings may map to a malformed target encoding. The eventual maps
must state explicit polynomial bounds. Counts, rather than an expanded list of
jobs, are the witnesses; their encoding has polynomial length in the target
input. Machine order has no effect on this feasibility predicate.

## Literature and significance

Koutecký and Zink, [Journal of Scheduling 28 (2025)](https://link.springer.com/article/10.1007/s10951-024-00827-8),
Theorem 4.14, prove NP-hardness with four job types. The paragraph following
that proof and Section 5.2 explicitly leave smaller type counts open. Lemma
4.8 supplies the balanced source transformation. The relevant result is ordinary
NP-hardness with a fixed type count; the paper's parameterized results are not
this target. The [arXiv record](https://arxiv.org/abs/2009.11840) traces the work
to its 2020 preprint and ISAAC version.

The [ICALP 2025 uniform-machine algorithm](https://drops.dagstuhl.de/storage/00lipics/lipics-vol334-icalp2025/html/LIPIcs.ICALP.2025.126/LIPIcs.ICALP.2025.126.html)
has a different machine model and parameter dependence. Its abstract does not
settle this three-type, binary-multiplicity unrelated-machine question; its
full proof was not audited. No matching later resolution was located in the
searches below. Unindexed, unpublished and overlooked results remain outside
coverage.

**Importance: moderate.** Success would lower the known fixed-type hardness
boundary for a standard scheduling model. It would not by itself classify the
two-type case or prove an approximation lower bound.

## Initial investigation

The first proposed route merges two counting roles from the four-type reduction.
It retains a machine-selecting blocker and two remaining job types. This is a
route diagnostic, not an original completed reduction or a research round.

Executed [probe](../evidence/three-type-unrelated-scheduling/probe.py) and
[raw evidence](../evidence/three-type-unrelated-scheduling/output.jsonl):
24 finite source instances, 12 YES and 12 NO, chosen deterministically from
sorted lists of four or six entries in {1,...,5}, with even total and blockers
larger than half the proposed makespan. There were 48 exact integer Z3 queries:
24 for the published baseline and 24 for the proposed merger. The baseline
agreed with exhaustive source checks. The merger accepted all twelve NO cases.
All returned schedules passed direct count and capacity checks. No timeout,
unknown-to-NO conversion, independent review, or full-candidate recovery test.

For example, source (1,3,3,3) is NO. The proposed three-type instance has
multiplicities (10,15,2), threshold 10000, and processing-time rows
(1009,999,8991), followed by three copies of (1007,997,6979).
Its feasible allocation is
(9,0,0), (0,10,0), (0,3,1), (1,2,1).
The merger allows counting jobs to move between the intended machine groups,
so a feasible schedule no longer determines a balanced partition.

Reproduce from the repository root:
`python3 research/evidence/three-type-unrelated-scheduling/probe.py`.
This bounded failure excludes the displayed merger, not all three-type reductions.

## Assessment and next test

Gates 1–4 pass within the stated literature coverage. Gate 5 is on hold:
arbitrary allocations can bypass the intended two choices. Gate 6 is not passed;
the executed diagnostic does not establish a viable remaining proof route.
Difficulty is **uncertain**, with no basis for a moderate rating yet.

The next bounded task is to test a redesigned three-type arithmetic selector
that forces two decodable allocation modes on each item machine while preserving
the global count equalities. Start by checking unwanted allocations with integer
constraints; require an argument bounding all allocations before scaling the
construction. A one-type reduction in the known construction is not sufficient
unless both directions and recovery survive. Stop this route if it only enforces
one side of the partition equality.

Experience retrieval searched `scheduling|multiplicity|partition|job types` in
the board and shared experience records. No applicable scheduling construction
was found. Geometry and cut entries have incompatible mathematical premises.
No shared experience entry was created for this initial failed merger.

## Search record — 2026-09-16

Queries included:

- `"unrelated machines" "three job types" hardness`
- `"unrelated machines" "3 job types" NP-hard`
- `"related machines" "five job types" hardness`
- `"Complexity of scheduling few types" 2026 2025 three`
- `"high multiplicity" "three" "unrelated" scheduling complexity 2026`
- `"high-multiplicity" "three job" scheduling`
- `"few types" "scheduling" "2026" hardness`

Read the primary journal proof of Theorem 4.14 and its preceding source
construction, the explicit open-question paragraph, Section 5.2, the arXiv
record, and the related ICALP abstract. No formal campaign budget has started;
the previous mixed-layout allocation is exhausted and is not transferred.
