cargo_ton_premise = 8723.0
unloaded_cargo_ton_premise = 5973.0
cargo_ton_hypothesis = 2754.0

# the hypothesis refers to the number of cargo tons, which are also mentioned in the premise
# compute the number of cargo tons left on the ship from the premise
cargo_ton_left_premise = cargo_ton_premise - unloaded_cargo_ton_premise
if cargo_ton_hypothesis!= cargo_ton_left_premise:
    # check if the number of cargo tons left on the ship from the hypothesis contradicts the number of cargo tons left on the ship from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
