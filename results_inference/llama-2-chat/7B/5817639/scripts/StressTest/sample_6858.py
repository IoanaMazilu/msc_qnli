rate_premise = 4
rate_hypothesis = 3

# the hypothesis refers to the rate of walking in miles per hour, which is also mentioned in the premise
if rate_hypothesis <= rate_premise:
    # check if the hypothesis value contradicts the estimate of the rate of walking in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the rate of walking,
    # any rate of walking greater than 'rate_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
