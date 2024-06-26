boxes_premise = 5
boxes_hypothesis = 8

# the hypothesis refers to the number of boxes in one case mentioned in the premise
if boxes_premise >= boxes_hypothesis:
    # check if the estimate of 'boxes_hypothesis' contradicts the number of boxes in the premise
    label = "contradiction"
elif boxes_premise < boxes_hypothesis:
    # if the number of boxes in the hypothesis is less than the number of boxes in the premise, we can infer entailment
    label = "entailment"
else:
    # if the number of boxes in the hypothesis is equal to the number of boxes in the premise, we can infer neutrality
    label = "neutral"

print(label)
