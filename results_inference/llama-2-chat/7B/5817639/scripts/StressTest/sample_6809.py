walking_rate_premise = 3
walking_rate_hypothesis = 5

# the hypothesis talks about the walking rate of two people, referenced also in the premise
if walking_rate_hypothesis <= walking_rate_premise:
    # check if the hypothesis value contradicts the estimate of 'walking_rate_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the walking rate, any other value is consistent with the premise but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
