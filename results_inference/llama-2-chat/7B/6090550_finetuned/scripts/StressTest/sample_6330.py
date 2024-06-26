boxes_premise = 5
boxes_hypothesis = 8

# the hypothesis refers to the number of boxes in a case, which is also mentioned in the premise
if boxes_hypothesis <= boxes_premise:
    # check if the hypothesis value contradicts the number of boxes in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise, we can infer entailment
    label = "entailment"

print(label)
