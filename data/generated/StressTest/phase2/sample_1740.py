# Premise: Sandy invested a certain sum of money at 12% p.
# Hypothesis: Sandy invested a certain sum of money at less than 82% p.
# Golden Label: entailment

investment_rate_premise = 12
investment_rate_hypothesis = 82

# the hypothesis refers to the rate of investment mentioned in the premise
if investment_rate_hypothesis <= investment_rate_premise:
    # check if the hypothesis value contradicts the value from the premise
    label = "contradiction"
else:
    # if the hypothesis value and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

