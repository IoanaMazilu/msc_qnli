# Premise: How many hours does it take Little Texas Drilling Company to produce 265 barrels of oil?
# Hypothesis: How many hours does it take Little Texas Drilling Company to produce more than 165 barrels of oil?
# Golden Label: entailment

oil_production_premise = 265
oil_production_hypothesis = 165

# The hypothesis is about the time it takes to produce a certain amount of oil, referenced also in the premise
if oil_production_hypothesis >= oil_production_premise:
    # Check if the hypothesis value contradicts the specific amount of 'oil_production_premise'
    label = "contradiction"
else:
    # The premise gives a specific quantity of oil production
    # Any quantity less than 'oil_production_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

