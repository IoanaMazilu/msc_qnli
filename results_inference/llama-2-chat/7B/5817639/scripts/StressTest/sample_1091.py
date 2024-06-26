walking_rate_premise = 3
walking_rate_hypothesis = 4

# the hypothesis refers to the walking rate of Johnny, which is compared to the premise walking rate
if walking_rate_hypothesis <= walking_rate_premise:
    # check if the estimate of 'walking_rate_hypothesis' contradicts the number of km walked by Johnny in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the walking rate of Johnny,
    # any walking rate greater than 'walking_rate_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
