boxes_premise = 8
boxes_hypothesis = 5

# the hypothesis refers to the number of boxes of cigarettes in a case, also mentioned in the premise
if boxes_hypothesis >= boxes_premise:
    # check if the hypothesis value contradicts the estimate of less than 'boxes_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of boxes
    # any number of boxes less than 'boxes_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
