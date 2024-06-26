shirts_premise = 160
shirts_hypothesis = 560

# the hypothesis talks about the number of shirts bought, referenced also in the premise
if shirts_hypothesis <= shirts_premise:
    # check if the hypothesis value contradicts the estimate of'shirts_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of shirts
    # any number of shirts greater than'shirts_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
