shirts_bought_premise = 160
shirts_bought_hypothesis = 560

if shirts_bought_hypothesis <= shirts_bought_premise:
    # check if the hypothesis value contradicts the number of shirts bought in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of shirts bought
    # any number of shirts greater than'shirts_bought_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
