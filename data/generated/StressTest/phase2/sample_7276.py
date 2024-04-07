# Premise: Molly and Max are driving at a rate of less than 400 kilometers per hour.
# Hypothesis: Molly and Max are driving at a rate of 100 kilometers per hour.
# Golden Label: neutral

driving_rate_premise = 400
driving_rate_hypothesis = 100

# the hypothesis refers to the driving rate of Molly and Max, mentioned in the premise
if driving_rate_hypothesis >= driving_rate_premise:
    # check if the hypothesis value contradicts the estimate of less than 'driving_rate_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the driving rate
    # any driving rate less than 'driving_rate_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

