premise_amount = 450
hypothesis_amount = 750

# the hypothesis refers to the amount sold to George, which is mentioned in the premise
if hypothesis_amount <= premise_amount:
    # check if the estimate of 'hypothesis_amount' contradicts the amount sold in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the amount sold
    # any amount greater than 'premise_amount' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
