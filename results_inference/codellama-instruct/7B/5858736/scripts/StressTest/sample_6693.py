premise_amount = 14000
premise_time = 8
hypothesis_amount = 44000
hypothesis_time = 8

# the hypothesis refers to the amount withdrawn and the time period mentioned in the premise
if hypothesis_amount <= premise_amount:
    # check if the estimate of 'hypothesis_amount' contradicts the amount withdrawn in the premise
    label = "contradiction"
elif hypothesis_time!= premise_time:
    # check if the time period in the hypothesis contradicts the time period reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
