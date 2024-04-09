investment_period_premise = 6
investment_period_hypothesis = 7
amount_invested = 20000

# the hypothesis refers to the investment period and the amount invested, mentioned in the premise
if investment_period_hypothesis < investment_period_premise:
    # check if the hypothesis investment period contradicts the premise investment period
    label = "contradiction"
elif amount_invested!= 20000:
    # check if the amount invested in the hypothesis contradicts the amount invested in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
