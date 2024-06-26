premise_amount = 20000
premise_time = 6
hypothesis_amount = 20000
hypothesis_time = 7

# the hypothesis talks about the amount invested and the time period, referenced also in the premise
if hypothesis_amount <= premise_amount:
    # check if the hypothesis value contradicts the estimate of more than 'premise_amount'
    label = "contradiction"
elif hypothesis_time <= premise_time:
    # check if the hypothesis time period contradicts the estimate of more than 'premise_time'
    label = "contradiction"
else:
    # the premise gives only an estimate for the amount and time period
    # any number of roses greater than 'roses_vase_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
