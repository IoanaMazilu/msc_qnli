combinations_premise = 55
combinations_hypothesis = 45

# the hypothesis refers to the number of possible combinations in which Michael is not selected, also referenced in the premise
if combinations_hypothesis <= combinations_premise:
    # check if the estimate of 'combinations_hypothesis' contradicts the number of combinations in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of combinations
    # any number of combinations greater than 'combinations_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
