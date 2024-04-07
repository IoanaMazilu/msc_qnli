# Premise: How many hours does it take Little Texas Drilling Company to produce more than 165 barrels of oil?
# Hypothesis: How many hours does it take Little Texas Drilling Company to produce 265 barrels of oil?
# Golden Label: neutral

oil_production_premise = 165
oil_production_hypothesis = 265

# the hypothesis refers to the number of barrels produced by Little Texas Drilling Company mentioned in the premise
if oil_production_hypothesis <= oil_production_premise:
    # check if the number of barrels produced in the hypothesis contradicts the estimate of more than 'oil_production_premise' barrels in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the oil production
    # any number of barrels greater than 'oil_production_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

