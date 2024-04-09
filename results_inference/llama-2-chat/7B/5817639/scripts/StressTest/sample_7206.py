marks_premise = 99
marks_hypothesis = 45

# the hypothesis talks about the marks secured by Reema, referenced also in the premise
if marks_hypothesis <= marks_premise:
    # check if the hypothesis value contradicts the estimate of'marks_premise'
    label = "contradiction"
else:
    # the premise gives an estimate for the marks, and the hypothesis provides a different estimate that is consistent with the premise
    label = "neutral"

print(label)
