discount_premise = 288
discount_hypothesis = 888

# the hypothesis refers to the discount on the same sum for the same time mentioned in the premise
if discount_hypothesis!= discount_premise:
    # check if the discount in the hypothesis contradicts the discount reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)