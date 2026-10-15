# Verification oracle: valid objective cuts

The unrestricted Z3 run completed 326 inputs, including its 51-digit YES input. The final 51-digit NO query had not returned a decision. The process was interrupted to replace its encoding with mathematically redundant inequalities; no timeout or NO verdict was assigned. Completed evidence remains in verification-without-cuts.jsonl and the original checker in verify-without-cuts.py.

For any positive integer vector w and actual target row P, set q=min_j P_j/w_j using exact fractions. Nonnegative x with P.x<=T satisfies q(w.x)<=T, hence w.x<=floor(T/q). These bounds depend on actual emitted coefficients, not an assumed local selector formula. If their sum equals w.n, every bound is attained. Adding these equalities preserves every feasible target witness. The checker still enforces all original constraints and enumerates all resulting models. It imports neither candidate nor prepared checker.

The source-derived choice w is only a choice of a valid positive bound direction; its validity does not depend on the candidate theorem. Tiny exhaustive validation of the bound is recorded separately. The changed encoding justifies rerunning the verification scope; these are reruns, not additional source coverage or a new research round.
