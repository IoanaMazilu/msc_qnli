shirts_bought_premise = 860
shirts_bought_hypothesis = 160

# the hypothesis talks about the number of shirts bought by Vijay, referenced also in the premise
if shirts_bought_hypothesis >= shirts_bought_premise:
    # check if the hypothesis value contradicts the estimate of less than 'shirts_bought_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of shirts
    # any number of shirts less than 'shirts_bought_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
