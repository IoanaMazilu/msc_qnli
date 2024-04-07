# Premise: Sandy invested a certain sum of money at 8% p.
# Hypothesis: Sandy invested a certain sum of money at more than 8% p.
# Golden Label: contradiction

invest_rate_premise = 8
invest_rate_hypothesis = 8

# the hypothesis refers to the rate of investment mentioned in the premise
if invest_rate_hypothesis <= invest_rate_premise:
    # check if the hypothesis value contradicts the rate mentioned in the premise
    label = "contradiction"
else:
    # the premise gives the exact investment rate
    # any rate greater than 'invest_rate_premise' cannot be explicitly entailed from the premise but does not contradict it either
    label = "neutral"

print(label)

