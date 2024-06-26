premise_days = 25
hypothesis_days = 25

# the hypothesis refers to the number of days mentioned in the premise
if hypothesis_days <= premise_days:
    # check if the estimate of 'hypothesis_days' contradicts the number of days in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of days
    # any number of days greater than 'premise_days' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
