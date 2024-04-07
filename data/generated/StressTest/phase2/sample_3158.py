# Premise: Sandy invested a certain sum of money at 8% p.
# Hypothesis: Sandy invested a certain sum of money at 4% p.
# Golden Label: contradiction

investment_rate_premise = 8
investment_rate_hypothesis = 4

# the hypothesis refers to the same event in the premise, but with a different investment rate
if investment_rate_hypothesis != investment_rate_premise:
    # check if the investment rate in the hypothesis contradicts the investment rate mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis investment rate is the same as the one in the premise, we could infer entailment,
    # but this case is not possible due to the previous condition
    label = "neutral"

print(label)

