investment_period_premise = 6
investment_period_hypothesis = 7

# the hypothesis refers to the investment period mentioned in the premise
if investment_period_hypothesis < investment_period_premise:
    # check if the 'investment_period_hypothesis' contradicts the investment period in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
