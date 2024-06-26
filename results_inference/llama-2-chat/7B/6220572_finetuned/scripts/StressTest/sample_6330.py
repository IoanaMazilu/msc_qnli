boxes_premise = 5
boxes_hypothesis = 8

# the hypothesis refers to the number of boxes of cigarettes in one case, also mentioned in the premise
if boxes_hypothesis <= boxes_premise:
    # check if the hypothesis estimate contradicts the number of boxes in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of boxes
    # any number of boxes less than 'boxes_hypothesis' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
