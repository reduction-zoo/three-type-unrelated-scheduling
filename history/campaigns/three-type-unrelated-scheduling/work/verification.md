# Verification of the three-type rule

Candidate: [algorithm.py](algorithm.py), with [general proof](proof.md). Both command modes execute in fresh subprocesses. The prepared checker and additional checker import neither candidate implementation into their oracles. No mathematical mismatch was found.

The final [prepared run](../rounds/009/final-injection-output.jsonl) passes eight inputs (four YES/four NO), with eight successful recovery calls. It was repeated after explicit malformed-input handling and arbitrary-size integer serialization were added; the initial run is preserved. Six malformed inputs are explicitly rejected in [boundary evidence](../rounds/009/malformed-output.json).

The additional [verify.py](verify.py) run covers 327 inputs: 94 YES and 233 NO. It exhaustively covers sorted lists of length two/four over 1..7, length six over 1..4, the empty source, two permuted sources, and two 51-digit inputs. It makes 848 exact Z3 queries, enumerates all 521 feasible target matrices for those inputs, and successfully recovers all 521 corresponding source subsets. Actual targets and recovered subsets are in the [raw log](../rounds/009/verification-output.jsonl). Z3 version: 5.1.0.

The original unrestricted verification encoding completed 326 inputs before a manual interruption during the last large NO query. Its [completed results](../rounds/009/verification-without-cuts.jsonl), [checker](../rounds/009/verify-without-cuts.py), and [interruption](../rounds/009/interruption.txt) are preserved. The run was replaced with a mathematically equivalent encoding adding objective upper bounds derived from the actual processing rows. The [proof of those cuts](../rounds/009/oracle-change.md) does not assume the candidate's selector lemma. Its [finite audit](../rounds/009/objective-cut-output.json) checks 221632 feasible configuration/bound pairs. The full additional scope was then rerun as required for the changed oracle encoding. A canceled/unknown result was never interpreted as NO. No timeout was used.

Reproduce from the repository root:

```sh
python3 campaigns/three-type-unrelated-scheduling/work/check.py --candidate campaigns/three-type-unrelated-scheduling/work/algorithm.py
python3 campaigns/three-type-unrelated-scheduling/work/verify.py --candidate campaigns/three-type-unrelated-scheduling/work/algorithm.py
```

Finite enumeration does not establish correctness on all inputs. The local and global proofs, encoding bounds, novelty and significance received an [independent advance review](../reviews/affine-selector/review.md). Expert human assessment remains outstanding. Main-agent checks are separate programs, not an independent author.
