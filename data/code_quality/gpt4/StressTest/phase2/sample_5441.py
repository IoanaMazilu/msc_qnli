oil_barrels_premise = 195
oil_barrels_hypothesis = 195

# the hypothesis refers to the number of oil barrels produced by the Little Texas Drilling Company mentioned in the premise
if oil_barrels_hypothesis >= oil_barrels_premise:
    # check if the hypothesis value contradicts the exact number of 'oil_barrels_premise' in the premise
    label = "neutral"
else:
    # if the hypothesis value is less than the exact number of 'oil_barrels_premise' in the premise, it is a contradiction
    label = "contradiction"

print(label)
