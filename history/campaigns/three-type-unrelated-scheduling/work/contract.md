# Encoding and rule contract

Source: `{"items": [a_0, ...]}`, an even-length list of positive binary integers.
The empty list is allowed. A witness is a list of distinct indices containing
half the items and half their total sum. Odd totals are legal NO instances.

Target: `{"processing_times": [[p_ij]], "counts": [n_j], "threshold": T}`.
There is at least one machine and one to three types. Processing times are
positive integers, multiplicities and threshold are nonnegative integers.
A witness is an integer matrix with the same shape as the processing-time
matrix: nonnegative entries, prescribed column sums, and row loads at most T.
The count encoding is compact even when expanding all jobs would be exponential.

`python3 algorithm.py` reads a source JSON object and emits its target.
`python3 algorithm.py --extract` reads `{"source": ..., "target_solution": ...}`
and returns a source witness. These run in fresh processes. No solver is allowed
in the eventual maps. Malformed source encodings may map to `{"invalid": true}`,
which is outside the target language. Legal NO sources must still produce legal
target instances. Recovery must handle every valid target count matrix.
