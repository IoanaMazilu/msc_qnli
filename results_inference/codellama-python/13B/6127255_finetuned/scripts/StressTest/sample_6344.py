discount_premise = 288
discount_hypothesis = 888

# the hypothesis refers to the same discount mentioned in the premise
if discount_hypothesis!= discount_premise:
    # check if the discount in the hypothesis contradicts the discount reported in the premise
    label = "contradiction"
else:
    # if the discount in the hypothesis does not contradict the discount in the premise, we can infer entailment
    label = "entailment"

print(label)
