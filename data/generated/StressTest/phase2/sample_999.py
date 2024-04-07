# Premise: How many hours does it take Little Texas Drilling Company to produce 205 barrels of oil?
# Hypothesis: How many hours does it take Little Texas Drilling Company to produce less than 405 barrels of oil?
# Golden Label: entailment

oil_production_premise = 205
oil_production_hypothesis = 405

# Both premise and hypothesis refer to oil production of Little Texas Drilling Company
if oil_production_premise >= oil_production_hypothesis:
    # Check if the oil production in the premise contradicts the hypothesis estimation of less than 'oil_production_hypothesis'
    label = "contradiction"
else:
    # The premise gives a specific oil production amount
    # Any oil production less than 'oil_production_hypothesis' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

