rate_premise = 7
rate_hypothesis = 2

# the hypothesis talks about the rate of walking in miles per hour, referenced also in the premise
if rate_hypothesis <= rate_premise:
    # check if the hypothesis value contradicts the estimate of 'rate_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the rate of walking
    # any rate of walking greater than 'rate_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
