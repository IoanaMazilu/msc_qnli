premise_total = 160
hypothesis_total = 760

# the hypothesis refers to the total amount paid for renting the tool
if hypothesis_total <= premise_total:
    # check if the estimate of 'hypothesis_total' contradicts the total amount paid in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the total amount paid
    # any total amount greater than 'premise_total' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
