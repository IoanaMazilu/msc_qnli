average_premise = 7
average_hypothesis = 7

# the hypothesis talks about the score needed to raise the average by less than 7 points
if average_hypothesis <= average_premise:
    # check if the hypothesis value contradicts the estimate of the average in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the average, any score that raises the average by less than 7 points is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
