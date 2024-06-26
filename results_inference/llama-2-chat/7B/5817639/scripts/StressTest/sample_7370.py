marks_premise = 55
marks_hypothesis = 35

# the hypothesis talks about the average of marks in English and History, referenced also in the premise
if marks_hypothesis <= marks_premise:
    # check if the hypothesis value contradicts the estimate of the average of'marks_premise'
    label = "contradiction"
else:
    # the premise gives an estimate for the average of marks, and the hypothesis value is consistent with that estimate
    label = "neutral"

print(label)
