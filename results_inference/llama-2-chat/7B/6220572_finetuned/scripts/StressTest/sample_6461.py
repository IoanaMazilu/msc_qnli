investment_fund_premise = 62500
investment_fund_hypothesis = 52500
annual_return_premise = 20
annual_return_hypothesis = 20

# the hypothesis talks about the amount deposited in an investment fund and the annual return, referenced also in the premise
if investment_fund_hypothesis!= investment_fund_premise:
    # check if the amount deposited in the hypothesis contradicts the amount deposited in the premise
    label = "contradiction"
elif annual_return_hypothesis!= annual_return_premise:
    # check if the annual return in the hypothesis contradicts the annual return reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
