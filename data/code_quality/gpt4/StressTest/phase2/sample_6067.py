shops_premise_min = 0
shops_premise_max = 5
shops_hypothesis_min = 4
shops_hypothesis_max = 5

# the hypothesis refers to the number of shops in the town mentioned in the premise
if shops_hypothesis_min < shops_premise_min or shops_hypothesis_max > shops_premise_max:
    # check if the range of shops in the hypothesis contradicts the range of shops mentioned in the premise
    label = "contradiction"
elif shops_hypothesis_min == shops_premise_min and shops_hypothesis_max == shops_premise_max:
    # if the ranges match, we can infer entailment
    label = "entailment"
else:
    # if the hypothesis range does not contradict the premise range but does not match it either, we infer neutrality
    label = "neutral"

print(label)
