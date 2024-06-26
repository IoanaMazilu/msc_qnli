premise_amount = 20000
premise_time = 6
hypothesis_amount = 20000
hypothesis_time = 7

# the hypothesis refers to the amount invested by Rick and the time period
if hypothesis_amount <= premise_amount:
    # check if the hypothesis value contradicts the premise amount
    label = "contradiction"
elif hypothesis_time < premise_time:
    # check if the hypothesis time period contradicts the premise time period
    label = "contradiction"
else:
    # the premise gives only an estimate for the amount invested by Rick
    # any amount greater than 'premise_amount' and any time period greater than 'premise_time' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
