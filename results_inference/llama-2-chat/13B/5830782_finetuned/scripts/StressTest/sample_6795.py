deposit_premise = 62500
deposit_hypothesis = 22500
annual_return_premise = 8
annual_return_hypothesis = 8

# the hypothesis refers to the amount deposited by Lucy and the annual return rate of the investment fund
if deposit_premise < deposit_hypothesis:
    # check if the deposit amount in the hypothesis contradicts the deposit amount reported in the premise
    label = "contradiction"
elif annual_return_premise!= annual_return_hypothesis:
    # check if the annual return rate in the hypothesis contradicts the annual return rate reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
