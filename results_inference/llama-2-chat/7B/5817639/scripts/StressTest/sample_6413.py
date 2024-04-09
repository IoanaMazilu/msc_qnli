combinations_premise = 55
combinations_hypothesis = 45

# the hypothesis talks about the number of possible combinations in which Michael is not selected, referenced also in the premise
if combinations_hypothesis <= combinations_premise:
    # check if the hypothesis value contradicts the estimate of more than 'combinations_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of possible combinations
    # any number of possible combinations greater than 'combinations_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
