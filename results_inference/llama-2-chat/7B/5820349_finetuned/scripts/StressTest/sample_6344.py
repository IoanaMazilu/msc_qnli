discount_premise = 288
discount_hypothesis = 888

# the hypothesis refers to the discount mentioned in the premise
if discount_hypothesis!= discount_premise:
    # check if the discount value in the hypothesis contradicts the discount value in the premise
    label = "contradiction"
else:
    # if the discount values do not contradict, we can infer entailment
    label = "entailment"

print(label)
