average_premise = 0
average_hypothesis = 2

# the hypothesis talks about raising the average by more than 2 points, which is not consistent with the premise
if average_hypothesis <= average_premise:
    label = "contradiction"
else:
    # the premise only gives an estimate for the average, so any number greater than the estimate is consistent with it, but cannot be explicitly entailed from it
    label = "neutral"

print(label)
