# Round 3 — Modular completion bonuses

## Plan

Change the round-2 premise: allow many jobs of type three on a machine. Let
A=sum a_i and T=(A+1)^4 product_i a_i. Machine i has processing times
(T/a_i-a_i-1, T/a_i, a_i), with global multiplicities (A/2,A/2,A/2+m/2).
The first two types must fill a_i slots per machine. Writing their first count
as x_i, the remaining constraint is a_i z_i<=(a_i+1)x_i. At x_i=a_i,
the machine earns one extra selector job beyond z_i=x_i; at intermediate
counts it does not. Test whether requiring m/2 such bonuses encodes balanced
partition or merely permits completion of the cheapest half plus partial fills.
Scope: inspect the exact local inequality and construct or refute schedules
on the same 24 screening sources. Reuse source evidence, not old target answers.
This family is outside the binary-selector lemma and has polynomial output
bit length despite potentially large integer values. Use the two pending
findings from rounds 1–2; universal recovery remains necessary for success.

## Evidence and diagnosis

The construction is again YES for every nonempty positive even-length source
with even total. First, T>a_i(a_i+1)^2 ensures that no machine can process
a_i+1 jobs of the first two types, even if every one uses the smaller processing
time. Their global count is A, so every machine must process exactly a_i of
these jobs. Its capacity then reduces to

\[
z_i\le x_i+\left\lfloor x_i/a_i\right\rfloor,\qquad 0\le x_i\le a_i.
\]

Choose the smallest m/2 items and fill their first-type counts completely.
Their sum is at most A/2. Add arbitrary partial first-type fills on the
remaining machines until their total reaches A/2. Set z_i=x_i+1 on the chosen
machines and z_i=x_i elsewhere. This meets every global count and capacity.
Thus earning the requested bonuses does not require a balanced subset: partial
fills absorb the difference. T has O(sum log(a_i)+log A) bits, so this failure
is not due to an encoding blow-up or numeric approximation.

[Output](output.jsonl) contains 24 directly validated schedules, twelve for
NO sources. The selected sources comprise 23 four-item and 1 six-item instances. Zero new solver
queries, no repairs/reruns; time/token unavailable. No full reduction, extractor,
independent review or novelty claim.

Experience extraction: extend the pending one-sided-capacity finding from
[round 1](../001/round.md) with this distinct modular family and its general
partial-fill counter-construction. The binary-selector theorem does not apply
here because z_i can exceed one. Shared destination remains blocked; no new
entry is counted for the same failure mechanism.

## Next action

Stop at 3/3 rounds. The tested full-blocker and completion-bonus families are
always YES, while the fixed-fill binary-selector abstraction is tractable.
These results do not classify unrestricted three-type scheduling. A next
attempt needs a mechanism enforcing both source bounds while allowing variable
fill totals or nonbinary selectors. No supported such construction is available
from this allocation, so immediate prospects are low and uncalibrated.
Reproduce with `python3 campaigns/three-type-unrelated-scheduling/rounds/003/probe.py`.

## Shared experience consolidation — 2026-09-16

After explicit user authorization, the finding and its recorded qualifications
were saved in [One-sided partition capacity](../../../../research/experience/one-sided-partition-capacity.md).
The pending status above describes the original round closure and is now
resolved. The use history distinguishes round-level findings from later shared
publication; no research tests were rerun for this documentation transfer.
