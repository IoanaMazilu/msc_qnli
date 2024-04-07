# Premise: How many hours does it take Little Texas Drilling Company to produce less than 500 barrels of oil?
# Hypothesis: How many hours does it take Little Texas Drilling Company to produce 100 barrels of oil?
# Golden Label: neutral

oil_production_premise = 500
oil_production_hypothesis = 100

# The hypothesis refers to the number of barrels produced by the Little Texas Drilling Company mentioned in the premise
if oil_production_hypothesis >= oil_production_premise:
    # Check if the production value in the hypothesis contradicts the estimate of less than 'oil_production_premise'
    label = "contradiction"
else:
    # The premise gives only an estimate for the oil production
    # Any production less than 'oil_production_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

