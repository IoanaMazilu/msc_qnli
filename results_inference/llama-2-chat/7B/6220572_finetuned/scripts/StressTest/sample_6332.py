boxes_premise = 5
boxes_hypothesis = 1

# the hypothesis talks about the number of boxes in a case, referenced also in the premise
if boxes_hypothesis!= boxes_premise:
    # check if the number of boxes in the hypothesis contradicts the number of boxes reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of boxes
    # any number of boxes consistent with 'boxes_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
