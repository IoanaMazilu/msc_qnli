walking_rate_premise = 2
walking_rate_hypothesis = 7

# the hypothesis talks about the rate of walking in miles per hour, referenced also in the premise
if walking_rate_hypothesis <= walking_rate_premise:
    # check if the hypothesis value contradicts the estimate of more than 'walking_rate_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the rate of walking
    # any rate of walking greater than 'walking_rate_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
