deposit_premise = 72500
deposit_hypothesis = 62500
return_premise = 20
return_hypothesis = 20

# the hypothesis refers to the amount deposited and the return mentioned in the premise
if deposit_hypothesis <= deposit_premise:
    # check if the estimate of 'deposit_hypothesis' contradicts the amount deposited in the premise
    label = "contradiction"
elif return_hypothesis!= return_premise:
    # check if the return in the hypothesis contradicts the return mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
