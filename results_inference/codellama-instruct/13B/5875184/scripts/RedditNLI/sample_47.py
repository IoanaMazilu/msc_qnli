premise_amount = 5.12
hypothesis_amount = 1000

# the hypothesis and premise mention the amount of money in the current account deficit
if hypothesis_amount < premise_amount:
    # check if the amount in the hypothesis contradicts the amount in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the amount
    # any estimate of the amount in the hypothesis greater or equal to 'premise_amount' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
