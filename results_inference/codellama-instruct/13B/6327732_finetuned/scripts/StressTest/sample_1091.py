matthew_walking_rate_premise = 3
matthew_walking_rate_hypothesis = 4

# the hypothesis refers to the walking rates mentioned in the premise
if matthew_walking_rate_hypothesis <= matthew_walking_rate_premise:
    # check if the estimate of'matthew_walking_rate_hypothesis' contradicts the number of km walked in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of km walked
    # any number of km greater than'matthew_walking_rate_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
