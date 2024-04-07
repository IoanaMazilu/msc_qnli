# Premise: How many hours does it take Little Texas Drilling Company to produce less than 815 barrels of oil?
# Hypothesis: How many hours does it take Little Texas Drilling Company to produce 115 barrels of oil?
# Golden Label: neutral

oil_production_premise = 815
oil_production_hypothesis = 115

# the hypothesis refers to the oil production of Little Texas Drilling Company mentioned in the premise
if oil_production_hypothesis >= oil_production_premise:
    # check if the oil production in the hypothesis contradicts the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the oil production
    # any oil production less than 'oil_production_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

