# Premise: How many hours does it take Little Texas Drilling Company to produce less than 405 barrels of oil?
# Hypothesis: How many hours does it take Little Texas Drilling Company to produce 205 barrels of oil?
# Golden Label: neutral

oil_production_premise = 405
oil_production_hypothesis = 205

# the hypothesis talks about the number of barrels of oil produced, referenced also in the premise
if oil_production_hypothesis >= oil_production_premise:
    # check if the hypothesis value contradicts the estimate of less than 'oil_production_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of barrels of oil
    # any number of barrels less than 'oil_production_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

