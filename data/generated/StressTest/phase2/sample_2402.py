# Premise: How many hours does it take Little Texas Drilling Company to produce 115 barrels of oil?
# Hypothesis: How many hours does it take Little Texas Drilling Company to produce less than 115 barrels of oil?
# Golden Label: contradiction

oil_prod_premise = 115
oil_prod_hypothesis = 115

# the hypothesis refers to the number of barrels of oil produced by Little Texas Drilling Company, which is also referenced in the premise
if oil_prod_hypothesis >= oil_prod_premise:
    # check if the hypothesis value contradicts the estimate of less than 'oil_prod_hypothesis'
    label = "contradiction"
else:
    # the premise gives only an exact value for the number of barrels
    # any number of barrels less than 'oil_prod_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

