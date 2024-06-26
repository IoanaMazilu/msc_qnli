deposit_premise = 62500
deposit_hypothesis = 72500
return_rate_premise = 20
return_rate_hypothesis = 20

# the hypothesis refers to the amount Lucy deposited and the return rate of the investment fund, both mentioned in the premise
if deposit_hypothesis <= deposit_premise:
    # check if the value of 'deposit_hypothesis' contradicts the deposit amount in the premise
    label = "contradiction"
elif return_rate_hypothesis != return_rate_premise:
    # check if the return rate in the hypothesis contradicts the return rate reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
