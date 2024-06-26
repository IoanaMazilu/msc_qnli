water_stored_premise = 14
water_stored_hypothesis = 34

# the hypothesis refers to the amount of water stored mentioned in the premise
if water_stored_hypothesis != water_stored_premise:
    # check if the amount of water stored in the hypothesis contradicts the amount of water stored reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
