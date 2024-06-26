shirts_bought_premise = 160
shirts_bought_hypothesis = 160

# the hypothesis refers to the number of shirts bought by Vijay mentioned in the premise
if shirts_bought_hypothesis >= shirts_bought_premise:
    # check if the hypothesis value contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis value is less than the premise, it can be entailed from the premise
    label = "entailment"

print(label)
# 