cargo_premise = 8723.0
cargo_unloaded_premise = 5973.0
cargo_hypothesis = 2754.0

# compute the remaining cargo on the ship based on the premise
remaining_cargo_premise = cargo_premise - cargo_unloaded_premise

if cargo_hypothesis > remaining_cargo_premise:
    # check if the remaining cargo in the hypothesis contradicts the estimate of remaining cargo from the premise
    label = "contradiction"
elif cargo_hypothesis!= remaining_cargo_premise:
    # check if the amount of cargo in the hypothesis contradicts the amount of cargo from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
