premise_deposit = 72500
hypothesis_deposit = 62500
annual_return = 20
compounding_frequency = 4

# the hypothesis refers to the number of deposited funds mentioned in the premise
if hypothesis_deposit <= premise_deposit:
    # check if the estimate of 'hypothesis_deposit' contradicts the number of deposited funds in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of deposited funds
    # any number of deposited funds greater than 'premise_deposit' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
