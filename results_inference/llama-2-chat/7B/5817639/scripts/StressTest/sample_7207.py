marks_premise = 45
marks_hypothesis = 35

# the hypothesis talks about the marks secured by Reema, referenced also in the premise
if marks_hypothesis <= marks_premise:
    # check if the hypothesis value contradicts the estimate of the average marks in the premise
    label = "contradiction"
else:
    # the premise gives an estimate for the average marks, and the hypothesis provides a different value
    # any value greater than the premise estimate is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
