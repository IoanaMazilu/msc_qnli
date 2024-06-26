combinations_premise = 4
combinations_hypothesis = 2

# the hypothesis refers to the number of combinations of passengers, which is also mentioned in the premise
if combinations_hypothesis <= combinations_premise:
    # check if the hypothesis value contradicts the estimate of 'combinations_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of combinations
    # any number of combinations greater than 'combinations_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
