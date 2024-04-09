premise_amount = 750
hypothesis_amount = 450

# the premise mentions a price for the item sold to George
if hypothesis_amount <= premise_amount:
    # check if the hypothesis value contradicts the estimate of less than 'premise_amount'
    label = "contradiction"
else:
    # the premise gives only an estimate for the amount sold to George
    # any amount less than or equal to 'premise_amount' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
