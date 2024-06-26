walking_rate_premise = 3
walking_rate_hypothesis = 5

# the hypothesis refers to the walking rates of Yolanda and Bob mentioned in the premise
if walking_rate_hypothesis <= walking_rate_premise:
    # check if the hypothesis value contradicts the walking rate in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the walking rate
    # any walking rate less than 'walking_rate_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
