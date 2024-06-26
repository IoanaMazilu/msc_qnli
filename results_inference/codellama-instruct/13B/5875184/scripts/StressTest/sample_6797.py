premise_amount = 62500
hypothesis_amount = 50000

# the hypothesis refers to the amount deposited in the investment fund
if hypothesis_amount < premise_amount:
    # check if the estimate of 'hypothesis_amount' contradicts the amount deposited in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the amount deposited
    # any amount greater than 'premise_amount' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
