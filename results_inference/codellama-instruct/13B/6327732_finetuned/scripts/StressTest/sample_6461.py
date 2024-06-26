deposit_premise = 62500
deposit_hypothesis = 52500
return_premise = 20
return_hypothesis = 20

# the hypothesis refers to the same investment fund and return rate as the premise
if deposit_hypothesis <= deposit_premise:
    # check if the estimate of 'deposit_hypothesis' contradicts the deposit amount in the premise
    label = "contradiction"
elif return_hypothesis!= return_premise:
    # check if the return rate in the hypothesis contradicts the return rate reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
