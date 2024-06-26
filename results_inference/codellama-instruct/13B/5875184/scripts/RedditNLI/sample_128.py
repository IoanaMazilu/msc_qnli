premise_amount = 7.2
hypothesis_amount = 7.15

# the hypothesis and premise mention the amount of money paid by Nestle to Starbucks
if hypothesis_amount < premise_amount:
    # check if the amount in the hypothesis contradicts the amount in the premise
    label = "contradiction"
else:
    # the premise gives an estimate for the amount paid by Nestle to Starbucks
    # any estimate of the amount in the hypothesis greater or equal to 'premise_amount' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
