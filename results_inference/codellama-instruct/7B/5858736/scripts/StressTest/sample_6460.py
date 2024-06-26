premise_deposit = 72500
hypothesis_deposit = 62500

# the hypothesis talks about the amount of money deposited in the investment fund
if hypothesis_deposit <= premise_deposit:
    # check if the hypothesis value contradicts the estimate of 'premise_deposit'
    label = "contradiction"
else:
    # the premise gives only an estimate for the amount of money deposited
    # any amount greater than 'premise_deposit' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
