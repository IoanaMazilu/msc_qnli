walking_rate_premise = 3
walking_rate_hypothesis = 5

# the hypothesis talks about the walking rate of Yolanda and Bob, referenced in the premise
if walking_rate_hypothesis <= walking_rate_premise:
    # check if the hypothesis value contradicts the estimate of Yolanda's walking rate in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for Yolanda's walking rate
    # any walking rate less than 'walking_rate_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
