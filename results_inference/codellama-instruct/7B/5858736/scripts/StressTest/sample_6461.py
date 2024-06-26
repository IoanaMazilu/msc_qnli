premise_deposit = 62500
hypothesis_deposit = 52500
premise_return = 0.20
hypothesis_return = 0.20

# the hypothesis talks about the amount deposited and the return rate, referenced also in the premise
if hypothesis_deposit <= premise_deposit:
    # check if the hypothesis value contradicts the estimate of more than 'premise_deposit'
    label = "contradiction"
elif hypothesis_return!= premise_return:
    # check if the return rate in the hypothesis contradicts the return rate reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
