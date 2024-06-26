boxes_premise = 20
boxes_hypothesis = 10

# the hypothesis talks about the number of boxes packed by Kramer, referenced also in the premise
if boxes_hypothesis <= boxes_premise:
    # check if the hypothesis value contradicts the estimate of less than 'boxes_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of boxes
    # any number of boxes greater than 'boxes_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
