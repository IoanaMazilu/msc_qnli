cargo_tons_premise = 8723.0
cargo_tons_hypothesis = 2754.0

# the hypothesis refers to the amount of cargo left on the ship, which is also mentioned in the premise
# compute the total amount of cargo unloaded from the premise
total_cargo_unloaded_premise = cargo_tons_premise - cargo_tons_hypothesis
if total_cargo_unloaded_premise == 0:
    # if the amount of cargo unloaded contradicts the amount of cargo left on the ship, label it as contradiction
    label = "contradiction"
elif cargo_tons_hypothesis == 0:
    # if the amount of cargo left on the ship contradicts the amount of cargo unloaded, label it as contradiction
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
