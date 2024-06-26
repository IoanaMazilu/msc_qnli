premise_amount = 2000
hypothesis_amount = 7000

# the hypothesis refers to the amount withdrawn by Tony, which is mentioned in the premise
if hypothesis_amount <= premise_amount:
    # check if the estimate of 'hypothesis_amount' contradicts the amount mentioned in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the amount withdrawn by Tony
    # any amount greater than 'premise_amount' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
