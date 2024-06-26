premise_amount = 3600
premise_rate = 0.06
hypothesis_amount = 3600
hypothesis_rate = 0.06

# the hypothesis refers to the amount and rate of interest mentioned in the premise
if hypothesis_amount <= premise_amount:
    # check if the estimate of 'hypothesis_amount' contradicts the amount in the premise
    label = "contradiction"
elif hypothesis_rate!= premise_rate:
    # check if the rate of interest in the hypothesis contradicts the rate of interest reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
