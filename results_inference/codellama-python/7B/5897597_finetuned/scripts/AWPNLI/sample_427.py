total_cargo_premise = 8723.0
unloaded_cargo_premise = 5973.0
left_cargo_hypothesis = 2754.0

# the hypothesis refers to the number of tons of cargo left on the ship, which can be inferred from the premise
# compute the number of tons of cargo left on the ship in the premise
left_cargo_premise = total_cargo_premise - unloaded_cargo_premise
if left_cargo_hypothesis!= left_cargo_premise:
    # check if the number of tons of cargo left in the hypothesis contradicts the number of tons of cargo left from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
