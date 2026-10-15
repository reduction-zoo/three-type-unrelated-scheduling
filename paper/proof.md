# Three-type unrelated scheduling: candidate proof

The fixed target admits a deterministic polynomial-time Karp reduction from
Balanced Partition, with polynomial recovery from every feasible count matrix.
This is a candidate result pending independent review. Novelty and significance
are assessed separately in the round record.

## Definitions and construction

The source contains m positive integers a_i in binary, with m even. Write
A=sum a_i. A solution is a set of m/2 indices whose weights sum to A/2.
The target is exactly the count-allocation language in [contract](../algorithm/contract.md).

For a nonempty source with A even, set

\[
k=\max_i a_i,\quad H=4(k+1)^2,\quad w=(k,k+1,2k+1).
\]

For each item a=a_i define the auxiliary capacity and processing row

\[
b_i=(k+1)(2k+1-a),\quad s_i=a(2k+1-a),
\]
\[
p_i=(Hk+2k+1-a,\ H(k+1)+a,\ H(2k+1)),\qquad
C_i=H b_i+s_i.
\]

These auxiliary capacities need not be equal. To obtain one common makespan,
use positive integers

\[
T=\prod_i C_i,\qquad P_{ij}=\frac{T}{C_i}p_{ij}.
\]

The target has m machines, three types, processing rows P_i, makespan T, and counts

\[
n=\left(\frac A2,\ \frac m2(2k+1)-\frac A2,
\ \frac m2(k+1)-\frac A2\right).
\]

All counts are nonnegative because A<=mk. All processing times and capacities
are positive. For each row, P_i.x<=T is equivalent to p_i.x<=C_i.
There is no machine-dependent deadline in the emitted target.

The empty source maps to one machine with processing time 1, zero jobs and
deadline 0. A source with odd A maps to processing time 1, one job and deadline
0, a legal NO instance. Malformed source encodings map to an invalid target
encoding. The implementation uses JSON integer strings as a polynomially
equivalent serialization of binary integers and disables Python's decimal
digit limit.

## Local selector lemma

For 1<=a<=k, every feasible nonnegative integer configuration x has
w.x<=b_i. Equality holds precisely at

\[
u_i=(0,2k+1-a,0),\qquad v_i=(a,0,k+1-a).
\]

**Proof.** Write t_i=(2k+1-a,a,0), so p_i=H w+t_i.
All coordinates of t_i are nonnegative, and
s_i<=k(k+1)<H. If w.x>=b_i+1, then
p_i.x>=H(b_i+1)>C_i, a contradiction.

It remains to classify the configurations with w.x=b_i. Denote their coordinates
by (x,y,z). Reducing this equality modulo k+1 gives
x+z=r(k+1) for a nonnegative integer r. Also

\[
k(x+z)\le b_i\le2k(k+1),
\]

so r is 0, 1 or 2. If r=0, the configuration is u_i.
If r=1, substitution gives

\[
y+z=k+1-a,\qquad
(x,y,z)=v_i+q(1,1,-1),\quad 0\le q\le k+1-a.
\]

The perturbation cost is s_i+q(2k+1), so feasibility forces q=0.
If r=2, both inequalities above must be equalities. This requires a=1
and the configuration (2(k+1),0,0). Its perturbation cost is
4k(k+1)>2k=s_i, so it is infeasible. Finally, both u_i and v_i
have perturbation cost s_i and objective b_i, and therefore load exactly C_i.
This proves the lemma for every k>=1, including a=k=1.

## Global equivalence and universal recovery

The specified global counts satisfy

\[
w.n=(k+1)\bigl(m(2k+1)-A\bigr)=\sum_i b_i.
\]

For any feasible target matrix, summing the local objective bounds gives
equality. Every row must therefore be u_i or v_i by the local lemma.
Let S be the indices of the v_i rows. The first and third column sums imply

\[
\sum_{i\in S}a_i=A/2,\qquad
|S|(k+1)-A/2=m(k+1)/2-A/2.
\]

Thus |S|=m/2, and S solves Balanced Partition. This argument applies to
every valid target witness; it assumes neither optimality nor a preferred
solver model. The executable extractor scans the rows, selects those equal
to v_i, and returns their indices. It rejects noncanonical rows and failed
source-witness checks explicitly. For the empty source it returns the empty
set. Legal NO targets have no witness requiring extraction.

Conversely, given a balanced subset S, place v_i on machines in S and u_i
elsewhere. The local lemma makes each row feasible. The first and third
column sums have the prescribed values. The second column sum is

\[
\sum_{i\notin S}(2k+1-a_i)=\frac m2(2k+1)-\frac A2.
\]

This constructs a feasible target matrix and proves both directions.

## Determinism and binary bounds

Let ell=1+ceil(log_2(k+1)) and let L be the source bit length. The auxiliary
processing times are O(k^3), capacities O(k^4), and counts O(mk).
Their individual bit lengths are O(ell+log m). The product T has O(m ell)
bits, and each scaled processing time has O(m ell) bits. The complete
output has O(m^2 ell+m log m) bits, hence O(L^3) bits. The construction
uses O(m) multiplications and exact divisions on at most O(m ell)-bit
integers. Schoolbook arithmetic gives the conservative bound O(L^5) bit
operations, including polynomial integer serialization. It never expands
the job multiplicities and uses no solver, randomness or learned decisions.

Recovery reads m rows, forms their two expected configurations and checks the
selected cardinality and sum. Its bit cost is O(B^2), conservatively, where
B is the combined encoded length of the source and supplied witness. The
output is at most m indices, or O(m log m) bits.

The target language is in NP: each allocation entry is at most its type's
global multiplicity. An m-by-three count matrix has polynomial bit length,
and integer arithmetic checks its column sums and row loads in polynomial
time. Together with the standard NP-hardness of Balanced Partition, the
reduction establishes NP-completeness of the at-most-three-type target.
The construction does not prove strong NP-hardness or an approximation gap.

For completeness, ordinary Partition on positive b_1,...,b_r reduces to the
balanced source by appending r zero weights and then adding 1 to all 2r
weights. Any subset of the original weights can be padded with zeros to
cardinality r; shifting adds exactly r to either balanced side. This gives
positive source entries and preserves the partition equation in both
directions with polynomial encoding. It is a standard source reduction,
not part of the claimed new contribution.
