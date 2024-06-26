premise_amount = 3
hypothesis_amount = 7

# the hypothesis refers to the percentage of the amount given back to parents
if hypothesis_amount <= premise_amount:
    # check if the estimate of 'hypothesis_amount' contradicts the percentage given back to parents in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the percentage of the amount given back to parents
    # any percentage greater than 'premise_amount' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
