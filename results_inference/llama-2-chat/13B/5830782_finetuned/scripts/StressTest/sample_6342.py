discount_premise = 288
discount_hypothesis = 588

# the hypothesis refers to the discount mentioned in the premise
if discount_premise >= discount_hypothesis:
    # check if the estimate of 'discount_hypothesis' contradicts the discount in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
