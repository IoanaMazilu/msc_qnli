marks_premise = 50
marks_hypothesis = 70

# the hypothesis talks about the marks secured by Reema, referenced also in the premise
if marks_hypothesis <= marks_premise:
    # check if the hypothesis value contradicts the estimate of the marks in the premise
    label = "contradiction"
else:
    # the premise gives an estimate for the marks, and any other estimate consistent with that estimate is neutral
    label = "neutral"

print(label)
