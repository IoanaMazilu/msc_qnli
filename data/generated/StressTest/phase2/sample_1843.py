# Premise: Sandy invested a certain sum of money at more than 6% p.
# Hypothesis: Sandy invested a certain sum of money at 8% p.
# Golden Label: neutral

investment_rate_premise = 6
investment_rate_hypothesis = 8

# the hypothesis refers to the investment rate mentioned in the premise
if investment_rate_hypothesis <= investment_rate_premise:
    # check if the hypothesis value contradicts the estimate of more than 'investment_rate_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the investment rate
    # any rate greater than 'investment_rate_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

