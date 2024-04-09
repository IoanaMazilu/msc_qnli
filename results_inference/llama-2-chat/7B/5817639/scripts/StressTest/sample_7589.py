average_mark_premise = 86
average_mark_hypothesis = 86

# the hypothesis talks about the number of marks scored by Adam in an examination, referenced also in the premise
if average_mark_hypothesis <= average_mark_premise:
    # check if the hypothesis value contradicts the estimate of the average mark in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the average mark
    # any average mark greater than 'average_mark_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
