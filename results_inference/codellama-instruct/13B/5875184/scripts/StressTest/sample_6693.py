premise_amount = 14000
hypothesis_amount = 44000

# the hypothesis talks about the amount of money withdrawn by John
if hypothesis_amount < premise_amount:
    # check if the hypothesis value contradicts the premise amount
    label = "contradiction"
else:
    # the premise gives an estimate for the amount of money withdrawn by John
    # any amount greater than 'premise_amount' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
