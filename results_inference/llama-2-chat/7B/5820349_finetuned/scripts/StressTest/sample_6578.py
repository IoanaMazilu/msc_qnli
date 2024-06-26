shirts_bought_premise = 160
shirts_bought_hypothesis = 160

# the hypothesis refers to the number of shirts bought by Vijay, also mentioned in the premise
if shirts_bought_hypothesis >= shirts_bought_premise:
    # check if the hypothesis value contradicts the premise of buying less than'shirts_bought_premise' shirts
    label = "contradiction"
else:
    # the premise gives an exact number of shirts bought
    # any number of shirts less than'shirts_bought_premise' cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
