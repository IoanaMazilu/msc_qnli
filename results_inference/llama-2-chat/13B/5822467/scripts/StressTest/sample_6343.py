discount_premise = 588
discount_hypothesis = 288

# the hypothesis refers to the true discount on the same sum for the same time
if discount_hypothesis <= discount_premise:
    # check if the hypothesis value contradicts the estimate of 'discount_premise'
    label = "contradiction"
elif discount_premise!= discount_hypothesis:
    # check if the true discount in the hypothesis contradicts the true discount reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
