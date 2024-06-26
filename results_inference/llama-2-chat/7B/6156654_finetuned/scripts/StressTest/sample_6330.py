boxes_premise = 5
boxes_hypothesis = 8

# the hypothesis refers to the number of boxes in a case, which is also mentioned in the premise
if boxes_premise >= boxes_hypothesis:
    # check if the number of boxes in the premise contradicts the hypothesis
    label = "contradiction"
else:
    # if the number of boxes in the premise is less than the hypothesis, we can infer entailment
    label = "entailment"

print(label)
