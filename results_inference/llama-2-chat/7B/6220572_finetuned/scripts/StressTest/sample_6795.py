investment_fund_deposit_premise = 62500
investment_fund_deposit_hypothesis = 22500
annual_return_premise = 8
annual_return_hypothesis = 8

# the hypothesis refers to the deposit amount and annual return mentioned in the premise
if investment_fund_deposit_hypothesis <= investment_fund_deposit_premise:
    # check if the estimate of 'investment_fund_deposit_hypothesis' contradicts the deposit amount in the premise
    label = "contradiction"
elif annual_return_hypothesis!= annual_return_premise:
    # check if the annual return in the hypothesis contradicts the annual return reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
