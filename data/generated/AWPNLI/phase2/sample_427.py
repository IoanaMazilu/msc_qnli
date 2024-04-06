# Premise: A ship has 8723.0 tons of cargo and at the Bahamas, sailors unloaded 5973.0 tons of cargo.
# Hypothesis: 2754.0 tons of cargo is left on the ship.
# Golden Label: contradiction

total_cargo_premise = 8723.0
unloaded_cargo_premise = 5973.0
remaining_cargo_hypothesis = 2754.0

# The hypothesis refers to the remaining cargo, which is also mentioned in the premise
# Compute the remaining cargo in the premise
remaining_cargo_premise = total_cargo_premise - unloaded_cargo_premise
if remaining_cargo_hypothesis != remaining_cargo_premise:
    # Check if the remaining cargo in the hypothesis contradicts the remaining cargo from the premise
    label = "contradiction"
else:
    # If the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)

