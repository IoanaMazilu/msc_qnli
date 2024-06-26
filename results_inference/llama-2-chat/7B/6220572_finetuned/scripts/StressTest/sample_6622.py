# the hypothesis refers to the number of committees less than 5 people, consistent with the premise estimate
if hypothesis_committees > premise_committees:
    # check if the number of committees in the hypothesis contradicts the estimate of less than 'premise_committees'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of committees
    # any number of committees less than 'premise_committees' consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
