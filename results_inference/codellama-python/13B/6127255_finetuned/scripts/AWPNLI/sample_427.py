cargo_premise = 8723.0
unloaded_cargo_premise = 5973.0
left_cargo_hypothesis = 2754.0

# the hypothesis refers to the amount of cargo left on the ship, which is also mentioned in the premise
# compute the amount of cargo left on the ship in the premise
left_cargo_premise = cargo_premise - unloaded_cargo_premise
if left_cargo_hypothesis!= left_cargo_premise:
    # check if the amount of cargo left on the ship in the hypothesis contradicts the amount of cargo left on the ship from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
