premise_amount = 2000
hypothesis_amount = 5000

# the hypothesis talks about the amount of money withdrawn by Tony
if hypothesis_amount <= premise_amount:
    # check if the hypothesis value contradicts the premise amount
    label = "contradiction"
else:
    # the premise gives only an estimate for the amount of money withdrawn by Tony
    # any amount greater than 'premise_amount' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
