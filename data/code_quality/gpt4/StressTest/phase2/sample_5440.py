oil_production_premise = 495
oil_production_hypothesis = 195

# the hypothesis is asking about the time it takes to produce a certain amount of oil, referenced also in the premise
if oil_production_hypothesis >= oil_production_premise:
    # check if the production amount in the hypothesis contradicts the estimate of less than 'oil_production_premise'
    label = "contradiction"
else:
    # any production amount less than 'oil_production_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
