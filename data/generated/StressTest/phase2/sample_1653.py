# Premise: How many hours does it take Little Texas Drilling Company to produce 100 barrels of oil?
# Hypothesis: How many hours does it take Little Texas Drilling Company to produce less than 500 barrels of oil?
# Golden Label: entailment

oil_production_premise = 100
oil_production_hypothesis = 500

# The hypothesis is asking about the time it takes to produce a quantity of oil, which is also referenced in the premise
if oil_production_hypothesis < oil_production_premise:
    # check if the quantity in the hypothesis contradicts the quantity in the premise
    label = "contradiction"
else:
    # the premise does not give any information about how long it takes to produce more than 100 barrels of oil
    # therefore, the hypothesis cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

