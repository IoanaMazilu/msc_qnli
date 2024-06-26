store_z_premise = 90
store_z_hypothesis = 70

# the hypothesis refers to the price of store Z, which is also mentioned in the premise
if store_z_hypothesis < store_z_premise:
    # check if the price of store Z in the hypothesis contradicts the price of store Z in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise value, we can infer entailment
    label = "entailment"

print(label)
