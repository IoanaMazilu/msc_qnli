marks_premise = 86
marks_hypothesis = 36

# the hypothesis talks about the marks secured by Reema, referenced also in the premise
if marks_hypothesis <= marks_premise:
    # check if the hypothesis value contradicts the estimate of the average marks in the premise
    label = "contradiction"
else:
    # the premise gives an estimate for the average marks, and any value of marks that is consistent with that estimate is not necessarily entailed from the premise
    label = "neutral"

print(label)
