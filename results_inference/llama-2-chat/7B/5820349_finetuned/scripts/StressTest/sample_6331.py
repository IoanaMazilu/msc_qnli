boxes_premise = 8
boxes_hypothesis = 5

# the hypothesis refers to the number of boxes of cigarettes mentioned in the premise
if boxes_hypothesis >= boxes_premise:
    # check if the number of boxes in the hypothesis contradicts the premise
    label = "contradiction"
else:
    # if the number of boxes in the hypothesis is less than the premise, it does not contradict the premise
    # but it cannot be explicitly entailed from the premise either
    label = "neutral"

print(label)
