# Independent review: affine selector

Decision: **advance** to manuscript preparation and expert review. Date: 2026-09-16.

Correctness is supported by a general argument and independent executable checks. Novelty is supported within the primary-literature coverage below, with explicit remaining gaps. Significance meets the fixed question: ordinary NP-completeness for at most three job types on explicitly listed unrelated machines. This decision is not human verification or publication acceptance.

## Scope and independence

Read the repository README, fixed question, contract, algorithm, proof, preparation, verification, prepared checker, additional checker, round 9 record and oracle-change explanation; subsequently read round 4's literature record. Candidate and checkers were not edited or imported. The reviewer wrote only this directory and spawned no agents. No shared experience entry is a premise of the proof.

The independent [check.py](check.py) invokes both executable modes in fresh subprocesses for targeted tests, enumerates actual target configurations directly without Z3, and separately enumerates the local inequality. Its [output](check-output.jsonl) records:

- 210 local parameter pairs, all `1 <= a <= k <= 20`, and 321410 feasible configurations, with exactly the two claimed maximizers in every pair.
- Five source inputs, including empty, odd-total NO, even-total NO and permuted YES cases; complete direct enumeration gives five total target witnesses, all recovered correctly.
- A pair of 5001-digit equal source integers, both canonical target witnesses checked against actual emitted capacities/counts and both recovered. The emitted threshold has 132882 bits. This exercises serialization beyond Python's default decimal conversion ceiling.
- Reconciliation of the additional raw log: 327 inputs, 94 YES, 521 witnesses and 848 queries.

Reproduce: `python3 campaigns/three-type-unrelated-scheduling/reviews/affine-selector/check.py`.

## Correctness

No blocking proof gap or implementation mismatch was found.

**Local argument, proof.md:64–90.** Since `s=a(2k+1-a) <= k(k+1) < H`, the nonnegative perturbation rules out every integer configuration with objective above `b`. At objective `b`, reducing modulo `k+1` yields `x+z=r(k+1)`. The inequality bounding this sum permits only `r=0,1,2`. For `r=1`, substitution gives `y+z=k+1-a`, and hence `x=a+y`: the parameter `q` in the proof is exactly the nonnegative integer `y`. Every positive `q` raises perturbation cost by `2k+1` and is infeasible. For `r=2`, equality in `k(x+z)<=b<=2k(k+1)` also forces `y=z=0`, since the omitted contribution is `(k+1)(y+z)`. It then forces `a=1`, and the displayed excess perturbation excludes this last case. Thus the classification is exhaustive, including `k=1`. Both surviving rows exactly fill their local capacities.

**Composition and both directions, proof.md:94–124.** The count identity is exact. The sum of nonnegative deficits `b_i-w.x_i` is zero, so every row attains its own bound. There is no assumption that a solver chooses an optimum or a preferred witness. First-column equality recovers selected weight; third-column equality then recovers selected cardinality. The second column is automatically correct for a balanced source subset. Therefore arbitrary mixing between item machines cannot create an extra schedule. Positive diagonal rescaling by `T/C_i` preserves each row's entire feasible set, not only the designated endpoints. No ordering assumption enters feasibility.

**Executable maps.** `forward` implements those formulas exactly, including product rescaling and all three multiplicities. Empty input is YES and produces the sole count witness `[[0]]`; odd total is NO and produces a legal one-type impossible instance. The validation rejects nonpositive integers, Boolean entries and odd list length. `extract` recognizes precisely the proved endpoints and independently checks the resulting subset's sum and size. On a valid witness the rejection branches cannot fire. For odd-total sources there is no target witness to recover. Rejecting other supplied matrices is consistent with the contract; a general-purpose target-witness validator is not required of recovery.

**Bit bounds and determinism, proof.md:128–155.** Auxiliary capacities are polynomial in the numerical maximum, but their binary encodings are logarithmic in it. A product of `m` such capacities therefore has `O(m log(k+1))` bits, not exponentially many bits. The stated `O(L^3)` output and conservative `O(L^5)` construction bounds hold using schoolbook arithmetic and decimal serialization. No multiplicity is expanded. Recovery performs only comparisons, additions and a scan; its stated conservative quadratic bound in combined encoded input/witness length is adequate. Positive source Partition padding establishes the chosen balanced source's ordinary NP-hardness; polynomial count witnesses establish target membership in NP. Neither strong hardness nor an approximation gap follows.

**Verification foundation.** The extra checker's objective cuts are valid independently of the selector lemma: for any positive `w`, `q=min_j P_j/w_j` implies `P.x >= q(w.x)` for every nonnegative `x`. Flooring gives the stated bound, and exact equality of summed bounds to `w.n` forces each row to attain its bound. This reasoning uses actual emitted rows and exact rational arithmetic. The original constraints remain present, and model blocking includes every allocation entry. Thus the cut-based enumeration does not discard a possible counterexample to the candidate. The reported interrupted large query is not a NO result; the completed replacement encoding supplies that decision. These finite checks, and the preparation's small oracle cross-checks, are useful implementation evidence but cannot replace the general argument above.

## Novelty and primary-source coverage

Search date for all entries and queries below: **2026-09-16**.

1. [Koutecký and Zink, Journal of Scheduling (2025)](https://link.springer.com/article/10.1007/s10951-024-00827-8): inspected Theorem 4.14 and its proof, the immediately following paragraph, Theorem 4.15, and Section 5.2. The closest fixed-type result uses four types and rank two. Its proof separates machine groups using a blocker and two counting roles. It does not give the present three-type selector; its parameterized hardness theorem does not imply hardness at three fixed types. The post-proof paragraph explicitly leaves smaller type counts open. This supports the concrete boundary improvement, within subsequent-search coverage.

2. [McCormick, Smallwood and Spieksma (2001), author PDF](https://feb.kuleuven.be/public/u0037710/papers/mor2001paper.pdf): inspected Section 5, Theorem 5.1, printed p.43, and the discussion of three-type limitations in Sections 7 and 9. Section 5 explicitly embeds two-type unrelated machines in its multiple-resource model and states a polynomial algorithm. This is a positive result at two types, not a three-type hardness construction. Its full algorithmic proof was not independently re-proved here. The manuscript should not describe the two-type case as open solely from the narrower citation in the 2025 paper. Round 4 already records this nuance, and the current candidate theorem makes no such claim.

3. [Goemans and Rothvoss, arXiv version dated 2020](https://arxiv.org/pdf/1307.5108): inspected Theorems 1 and 2, Section 2, p.3. Their fixed-dimensional integer-cone formulation uses points from a common polytope. Our equivalent formulation requires one point from each of an input-dependent list of distinct three-dimensional integer knapsack sets. The common-polytope theorem does not directly solve or establish hardness of that constrained sum. In particular, fixed job-type dimension is not a bound on the total number of allocation variables or the number of distinct machine configurations. The present reduction explicitly implements the needed two-choice sets inside genuine one-inequality knapsacks; arbitrary finite-set subset-sum hardness alone would not establish this realization.

4. [Rohwedder, ICALP 2025](https://drops.dagstuhl.de/storage/00lipics/lipics-vol334-icalp2025/html/LIPIcs.ICALP.2025.126/LIPIcs.ICALP.2025.126.html): inspected Theorem 1 and the high-multiplicity discussion immediately after Theorem 2. The algorithm is for uniform machines and retains dependence on the numerical maximum processing time. It does not settle the present binary-encoded unrelated-machine endpoint. The full algorithm was not re-proved.

5. [Sun, rejection scheduling (2026)](https://link.springer.com/article/10.1007/s10878-026-01455-y): the publisher confirms the title and July 2026 publication; full text is subscription-restricted. This review does not claim to exclude every theorem in that paper. It remains an explicit coverage gap.

Queries included `"unrelated" "three job types" scheduling`, `"scheduling" "3 job types" hardness`, `"three" "job types" "NP-hard" 2026`, `"high multiplicity" "three" "unrelated" scheduling NP`, `"unrelated machines" "three types" complexity`, `"unrelated" "job types" "2026" hardness scheduling`, `"integer" "Minkowski sum" "knapsack" complexity`, `"McCormick" "unrelated" "two" scheduling error`, and the Goemans–Rothvoss title with unrelated-machine/theorem terms. No matching later theorem or immediate known-result implication was found. Unindexed work, unpublished work, inaccessible full text and alternate terminology remain outside exhaustive coverage. Absence from these searches is not proof of absolute originality.

## Significance and disposition

The concrete contribution is a three-coordinate local arithmetic selector whose globally forced choices recover both weight and cardinality. Together with exact common-deadline rescaling it lowers the located ordinary hardness boundary from four types to three under the fixed encoding. This is a meaningful complexity result, not production integration or a smaller implementation of an existing rule. Its dependence on large binary numbers is permitted by the fixed question. It does not warrant claims of strong NP-hardness, approximation hardness, or a new two-type classification.

The fixed question's screening-status prose is historical; the user authorized the investigation, and this review evaluates the unchanged mathematical endpoint. No change of acceptance criteria is needed. Proceed with the current maps and theorem. Preserve the literature coverage qualifications, especially the two-type nuance and inaccessible 2026 paper, in the manuscript and expert-review materials.
