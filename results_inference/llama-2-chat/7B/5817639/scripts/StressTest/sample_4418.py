average_premise = 85
average_hypothesis = 90

# the hypothesis talks about the score needed to raise the average by 5 points, while the premise talks about raising the average by 2 points
if average_hypothesis <= average_premise:
    # check if the hypothesis value contradicts the estimate of the score needed to raise the average by 2 points
    label = "contradiction"
else:
    # the premise gives an estimate for the score needed to raise the average by 2 points, while the hypothesis gives an estimate for the score needed to raise the average by 5 points
    # any score greater than the estimate in the premise is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
