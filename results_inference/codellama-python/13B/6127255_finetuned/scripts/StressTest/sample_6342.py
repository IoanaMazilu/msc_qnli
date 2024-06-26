discount_premise = 288
discount_hypothesis = 588

# the hypothesis refers to the discount mentioned in the premise
if discount_hypothesis <= discount_premise:
    # check if the hypothesis value contradicts the discount in the premise
    label = "contradiction"
elif discount_premise >= discount_hypothesis:
    # check if the discount in the premise contradicts the hypothesis
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise discount, we can infer entailment
    label = "entailment"

print(label)
#