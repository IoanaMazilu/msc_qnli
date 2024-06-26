premise_amount = 600000
premise_rate = 10
premise_period = 3

hypothesis_amount = 100000
hypothesis_rate = 10
hypothesis_period = 3

# the hypothesis refers to the amount invested and the interest rate mentioned in the premise
if hypothesis_amount <= premise_amount:
    # check if the estimate of 'hypothesis_amount' contradicts the amount invested in the premise
    label = "contradiction"
elif hypothesis_rate!= premise_rate:
    # check if the interest rate in the hypothesis contradicts the rate mentioned in the premise
    label = "contradiction"
elif hypothesis_period!= premise_period:
    # check if the period in the hypothesis contradicts the period mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
