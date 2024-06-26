premise_amount = 20000
premise_time = 6
hypothesis_amount = 20000
hypothesis_time = 7

# the hypothesis refers to a shorter time period than the premise
if hypothesis_time < premise_time:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
else:
    # the premise gives an estimate for the amount invested by Rick
    # any amount greater than 'premise_amount' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
