boxes_premise = 5
boxes_hypothesis = 8

# the hypothesis refers to the number of boxes of cigarettes in one case mentioned in the premise
if boxes_premise >= boxes_hypothesis:
    # check if the estimate of 'boxes_hypothesis' contradicts the number of boxes in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
