boxes_premise = 5
boxes_hypothesis = 8

# the hypothesis refers to the number of boxes of cigarettes mentioned in the premise
if boxes_premise >= boxes_hypothesis:
    # check if the number of boxes in the premise contradicts the hypothesis
    label = "contradiction"
elif boxes_premise < boxes_hypothesis:
    # if the number of boxes in the premise is less than the number in the hypothesis, we can infer entailment
    label = "entailment"

print(label)
