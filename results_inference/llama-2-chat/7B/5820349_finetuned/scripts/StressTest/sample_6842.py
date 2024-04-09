investment_period_premise = 6
investment_period_hypothesis = 6
investment_amount_premise = 20000
investment_amount_hypothesis = 20000

# the hypothesis talks about the investment period and amount, which are also mentioned in the premise
if investment_period_hypothesis <= investment_period_premise:
    # check if the hypothesis value contradicts the premise value for the investment period
    label = "contradiction"
elif investment_amount_hypothesis!= investment_amount_premise:
    # check if the hypothesis value contradicts the premise value for the investment amount
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
