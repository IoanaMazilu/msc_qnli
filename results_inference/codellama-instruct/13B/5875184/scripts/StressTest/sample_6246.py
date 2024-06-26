premise_amount = 100000
premise_rate = 10
premise_period = 3

hypothesis_amount = 600000
hypothesis_rate = 10
hypothesis_period = 3

# the hypothesis talks about the amount invested and the interest rate, both referenced in the premise
if hypothesis_amount <= premise_amount:
    # check if the hypothesis value contradicts the estimate of more than 'premise_amount'
    label = "contradiction"
elif hypothesis_rate!= premise_rate:
    # check if the interest rate in the hypothesis contradicts the rate mentioned in the premise
    label = "contradiction"
elif hypothesis_period!= premise_period:
    # check if the period in the hypothesis contradicts the period mentioned in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the amount invested and the interest rate
    # any amount and interest rate greater than 'premise_amount' and 'premise_rate' respectively, and a period of three years, is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
