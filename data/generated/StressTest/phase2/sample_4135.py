# Premise: Sandy invested a certain sum of money at less than 72% p.
# Hypothesis: Sandy invested a certain sum of money at 12% p.
# Golden Label: neutral

investment_rate_premise = 72
investment_rate_hypothesis = 12

# the hypothesis refers to the interest rate of Sandy's investment mentioned in the premise
if investment_rate_hypothesis >= investment_rate_premise:
    # check if the hypothesis value contradicts the estimate of less than 'investment_rate_premise' in the premise
    label = "contradiction"
elif investment_rate_hypothesis < investment_rate_premise:
    # the premise gives an upper limit for the interest rate
    # the hypothesis rate (which is less than the premise rate) is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

