deposit_amount = 62500
hypothesis_deposit_amount = 62500
interest_rate = 8
compounding_periods = 4

# the hypothesis refers to the deposit amount and the interest rate, which are also mentioned in the premise
if deposit_amount!= hypothesis_deposit_amount:
    # check if the deposit amount in the hypothesis contradicts the deposit amount in the premise
    label = "contradiction"
elif interest_rate!= 8 or compounding_periods!= 4:
    # check if the interest rate or compounding periods in the hypothesis contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
