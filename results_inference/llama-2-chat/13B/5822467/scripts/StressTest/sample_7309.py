typing_premise = 7
typing_hypothesis = 8

# the hypothesis talks about the number of words typed, referenced also in the premise
if typing_hypothesis <= typing_premise:
    # check if the hypothesis value contradicts the estimate of more than 'typing_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of words typed
    # any number of words greater than 'typing_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
