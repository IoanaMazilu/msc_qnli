shirts_premise = 160
shirts_hypothesis = float(hypothesis)

# check if the hypothesis value is less than or equal to the premise value
if shirts_hypothesis <= shirts_premise:
    # check if the hypothesis value contradicts the estimate of'shirts_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of shirts
    # any number of shirts greater than or equal to'shirts_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
