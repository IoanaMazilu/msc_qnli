marks_premise = 35
marks_hypothesis = 75

# the hypothesis talks about the marks secured by Reema, referenced also in the premise
if marks_hypothesis <= marks_premise:
    # check if the hypothesis value contradicts the estimate of the marks in the premise
    label = "contradiction"
else:
    # the premise gives an estimate for the marks, and any estimate greater than the premise is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
