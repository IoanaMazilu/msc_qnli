premise_amount = 20000
premise_time = 6
hypothesis_amount = 20000
hypothesis_time = 12

# the hypothesis refers to the time period mentioned in the premise
if hypothesis_time > premise_time:
    # check if the estimate of 'hypothesis_time' contradicts the time period in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the time period
    # any time period greater than 'premise_time' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
