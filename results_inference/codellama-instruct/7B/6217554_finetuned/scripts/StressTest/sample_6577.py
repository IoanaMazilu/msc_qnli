shirts_bought_premise = 560
shirts_bought_hypothesis = 160

if shirts_bought_hypothesis >= shirts_bought_premise:
    # check if the number of shirts bought in the hypothesis contradicts the estimate of less than'shirts_bought_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of shirts bought
    # any number of shirts bought less than'shirts_bought_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
