rate_premise = 4
rate_hypothesis = 4

# the premise gives a value for the rate of walking, and the hypothesis refers to the same rate
if rate_hypothesis <= rate_premise:
    # check if the hypothesis value contradicts the estimate of the rate of walking in the premise
    label = "contradiction"
else:
    # the premise gives a direct estimate for the rate of walking, and the hypothesis refers to the same rate
    # any rate of walking greater than the premise value is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
