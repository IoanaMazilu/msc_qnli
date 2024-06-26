walking_rate_premise = 3
walking_rate_hypothesis = 4

# the hypothesis talks about Jack's walking rate in miles per hour, referenced also in the premise
if walking_rate_premise <= walking_rate_hypothesis:
    # check if the estimate of 'walking_rate_hypothesis' contradicts the rate of walking in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for Jack's walking rate
    # any rate of walking greater than 'walking_rate_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
