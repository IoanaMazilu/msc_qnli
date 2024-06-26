combinations_premise = 45
combinations_hypothesis = 55

# the hypothesis refers to the number of combinations in which Michael is not selected, mentioned also in the premise
if combinations_hypothesis <= combinations_premise:
    # check if the hypothesis value contradicts the estimate of more than 'combinations_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of combinations
    # any number of combinations greater than 'combinations_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
