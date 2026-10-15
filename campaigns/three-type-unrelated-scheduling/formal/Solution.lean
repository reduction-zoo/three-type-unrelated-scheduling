module

public import Mathlib.Computability.TuringMachine.Computable

@[expose] public section

namespace ThreeTypeUnrelatedScheduling

/-- Q001's self-delimiting binary natural; length is logarithmic, not unary. -/
def encodeNat (n : Nat) : List Bool :=
  let bits := (Nat.toDigits 2 n).map (fun c => c == '1')
  List.replicate bits.length true ++ [false] ++ bits

def encodeList {α : Type} (encode : α → List Bool) (xs : List α) : List Bool :=
  encodeNat xs.length ++ xs.flatMap encode

def encodeOption {α : Type} (encode : α → List Bool) : Option α → List Bool
  | none => [false]
  | some x => true :: encode x

/-- None denotes mathematical nonexistence, never an execution error. -/
def searchOutput {I W : Type} (legal : I → Bool) (witness : I → W → Bool)
    (x : I) : Option W → Prop
  | some w => legal x = true ∧ witness x w = true
  | none => legal x = true ∧ ¬ ∃ w, witness x w = true

def legalSource (x : List Nat) : Bool := x.all (fun w => w > 0) && x.length % 2 == 0

def sourceWitness (x : List Nat) (subset : List Nat) : Bool :=
  decide subset.Nodup && subset.all (fun i => i < x.length) &&
  2 * subset.length == x.length &&
  2 * (subset.map (fun i => x[i]?.getD 0)).sum == x.sum

def encodeSource := encodeList encodeNat

def validSourceOutput := searchOutput legalSource sourceWitness

structure Instance where
  counts : List Nat
  processing : List (List Nat)
  bound : Nat
  deriving Repr
def legalTarget (x : Instance) : Bool :=
  x.counts.length == 3 && x.processing.all (fun row => row.length == 3 && row.all (fun p => p > 0))
def targetWitness (x : Instance) (w : List (List Nat)) : Bool :=
  w.length == x.processing.length && w.all (fun row => row.length == 3) &&
  (List.range 3).all (fun j => (w.map (fun row => row[j]?.getD 0)).sum == x.counts[j]?.getD 0) &&
  (w.zip x.processing).all (fun (counts,times) =>
    ((counts.zip times).map (fun (c,t) => c*t)).sum ≤ x.bound)
def encodeTarget (x : Instance) := encodeList encodeNat x.counts ++
  encodeList (encodeList encodeNat) x.processing ++ encodeNat x.bound
def validTargetOutput := searchOutput legalTarget targetWitness

/-- Both algorithms use Q001's explicit bit encoding and TM2 cost model.
Recovery receives the full pair of source instance and target output. -/
def Reduction (forward : (List Nat) → Instance)
    (recover : (List Nat) × Option (List (List Nat)) → Option (List Nat)) : Prop :=
  Nonempty (Turing.TM2ComputableInPolyTime encodeSource encodeTarget forward) ∧
  Nonempty (Turing.TM2ComputableInPolyTime
    (fun input => encodeSource input.1 ++ (encodeOption (encodeList (encodeList encodeNat))) input.2)
    (encodeOption (encodeList encodeNat)) recover) ∧
  (∃ bound : Polynomial Nat, ∀ x,
    (encodeTarget (forward x)).length ≤ bound.eval (encodeSource x).length) ∧
  (∃ bound : Polynomial Nat, ∀ input,
    ((encodeOption (encodeList encodeNat)) (recover input)).length ≤
      bound.eval (encodeSource input.1 ++ (encodeOption (encodeList (encodeList encodeNat))) input.2).length) ∧
  (∀ x, legalSource x = true → legalTarget (forward x) = true) ∧
  (∀ x, legalSource x = true → ∀ y, validTargetOutput (forward x) y →
    validSourceOutput x (recover (x, y)))

def Goal : Prop :=
  ∃ (forward : (List Nat) → Instance)
    (recover : (List Nat) × Option (List (List Nat)) → Option (List Nat)), Reduction forward recover

/-- Open question only; this placeholder is not a solution. -/
theorem solve : Goal := by
  sorry

end ThreeTypeUnrelatedScheduling
