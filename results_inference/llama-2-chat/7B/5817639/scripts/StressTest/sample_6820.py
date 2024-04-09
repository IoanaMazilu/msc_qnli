combinations_premise = 0
combinations_hypothesis = 2

# the hypothesis talks about the number of combinations Barbara has, referenced also in the premise
if combinations_hypothesis <= combinations_premise:
    # check if the hypothesis value contradicts the estimate of 'combinations_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of combinations
    # any number of combinations greater than 'combinations_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
