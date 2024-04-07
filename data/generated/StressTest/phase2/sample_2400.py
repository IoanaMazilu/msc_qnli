# Premise: How many hours does it take Little Texas Drilling Company to produce 115 barrels of oil?
# Hypothesis: How many hours does it take Little Texas Drilling Company to produce less than 815 barrels of oil?
# Golden Label: entailment

oil_production_premise = 115
oil_production_hypothesis = 815

# the hypothesis and premise both talk about the oil production of the Little Texas Drilling Company
if oil_production_hypothesis <= oil_production_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
else:
    # the premise gives a specific amount of oil production, while the hypothesis only gives an estimate
    # the premise value doesn't contradict the hypothesis, but it can't be fully and explicitly entailed from it
    label = "neutral"

print(label)

