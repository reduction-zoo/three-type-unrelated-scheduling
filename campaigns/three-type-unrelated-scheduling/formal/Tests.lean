import Challenge
open ThreeTypeUnrelatedScheduling
example : targetWitness ⟨[2,0,1], [[1,1,2],[2,1,1]], 2⟩ [[2,0,0],[0,0,1]] = true := by native_decide
example : targetWitness ⟨[2,0,1], [[1,1,2],[2,1,1]], 2⟩ [[2,0,1],[0,0,0]] = false := by native_decide
