boxes_cigarettes_premise = 8
boxes_cigarettes_hypothesis = 5

# the hypothesis talks about the number of boxes of cigarettes in one case, referenced also in the premise
if boxes_cigarettes_hypothesis >= boxes_cigarettes_premise:
    # check if the number of boxes of cigarettes in the hypothesis contradicts the estimate of less than 'boxes_cigarettes_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of boxes of cigarettes
    # any number of boxes of cigarettes less than 'boxes_cigarettes_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
