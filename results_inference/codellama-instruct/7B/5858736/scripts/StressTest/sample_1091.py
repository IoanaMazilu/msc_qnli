walking_rate_matthew_premise = 3
walking_rate_johnny_premise = 4

# the hypothesis refers to the walking rate of both individuals, mentioned in the premise
if walking_rate_matthew_premise > walking_rate_johnny_premise:
    # check if the estimate of 'walking_rate_matthew_premise' contradicts the walking rate of Johnny
    label = "contradiction"
else:
    # the premise gives only an estimate for the walking rate of Matthew
    # any walking rate greater than 'walking_rate_matthew_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
