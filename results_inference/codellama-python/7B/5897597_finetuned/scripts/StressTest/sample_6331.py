cigarettes_boxes_premise = 8
cigarettes_boxes_hypothesis = 5

# the hypothesis talks about the number of boxes of cigarettes in a case, referenced also in the premise
if cigarettes_boxes_hypothesis >= cigarettes_boxes_premise:
    # check if the hypothesis value contradicts the estimate of less than 'cigarettes_boxes_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of boxes
    # any number of boxes less than 'cigarettes_boxes_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
