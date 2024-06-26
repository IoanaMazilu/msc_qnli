premise_months = 2
hypothesis_months = 8

# the hypothesis refers to the number of months mentioned in the premise
if hypothesis_months >= premise_months:
    # check if the estimate of 'hypothesis_months' contradicts the number of months in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of months
    # any number of months less than 'premise_months' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
