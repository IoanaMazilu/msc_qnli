premise_amount = 20000
premise_duration = 6
hypothesis_amount = 20000
hypothesis_duration = 6

# the hypothesis refers to the amount invested by Rick for more than 6 months
if hypothesis_duration > premise_duration:
    # check if the hypothesis value contradicts the estimate of 'premise_duration'
    label = "contradiction"
else:
    # the premise gives only an estimate for the duration
    # any duration greater than 'premise_duration' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
