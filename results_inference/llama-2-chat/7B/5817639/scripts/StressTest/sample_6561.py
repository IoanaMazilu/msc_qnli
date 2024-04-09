average_premise = 7
average_hypothesis = 6

# the hypothesis talks about the score needed to raise the average by less than 6 points
if average_hypothesis <= average_premise:
    # check if the hypothesis value contradicts the estimate of the average in the premise
    label = "contradiction"
else:
    # the premise gives an estimate for the average, and the hypothesis value is consistent with it
    label = "neutral"

print(label)
