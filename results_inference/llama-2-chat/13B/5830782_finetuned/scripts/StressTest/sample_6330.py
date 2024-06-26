boxes_premise = 5
boxes_hypothesis = 8

# the hypothesis refers to the number of boxes of cigarettes in a case mentioned in the premise
if boxes_premise >= boxes_hypothesis:
    # check if the estimate of 'boxes_premise' contradicts the number of boxes in the hypothesis
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
