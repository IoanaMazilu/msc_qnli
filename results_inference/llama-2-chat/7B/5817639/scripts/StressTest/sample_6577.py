shirts_premise = 560
shirts_hypothesis = 160

# the hypothesis talks about the number of shirts bought at a rate, referenced also in the premise
if shirts_hypothesis <= shirts_premise:
    # check if the hypothesis value contradicts the estimate of less than'shirts_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of shirts bought
    # any number of shirts bought greater than'shirts_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
