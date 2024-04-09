deposit_premise = 62500
deposit_hypothesis = 52500
annual_return_premise = 20
annual_return_hypothesis = 20

# the hypothesis refers to the amount of money deposited and the annual return rate, both mentioned in the premise
if deposit_premise!= deposit_hypothesis:
    # check if the deposit amount in the hypothesis contradicts the deposit amount in the premise
    label = "contradiction"
elif annual_return_premise!= annual_return_hypothesis:
    # check if the annual return rate in the hypothesis contradicts the annual return rate in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
