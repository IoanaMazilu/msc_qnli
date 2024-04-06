# Premise: A ship has 8723.0 tons of cargo and at the Bahamas, sailors unloaded 5973.0 tons of cargo.
# Hypothesis: 2750.0 tons of cargo is left on the ship.
# Golden Label: entailment

total_cargo_premise = 8723.0
unload_cargo_premise = 5973.0
left_cargo_hypothesis = 2750.0

# the hypothesis refers to the amount of cargo left, which is also mentioned in the premise
# compute the amount of cargo left in the premise
left_cargo_premise = total_cargo_premise - unload_cargo_premise
if left_cargo_hypothesis != left_cargo_premise:
    # check if the amount of cargo left in the hypothesis contradicts the amount of cargo left from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)

