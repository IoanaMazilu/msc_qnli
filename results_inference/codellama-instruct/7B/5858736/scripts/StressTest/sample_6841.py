premise_amount = 20000
premise_time = 7
hypothesis_amount = 20000
hypothesis_time = 6

# the hypothesis talks about the amount invested and the time period, referenced also in the premise
if hypothesis_amount <= premise_amount:
    # check if the hypothesis value contradicts the estimate of 'premise_amount'
    label = "contradiction"
elif hypothesis_time <= premise_time:
    # check if the hypothesis value contradicts the estimate of 'premise_time'
    label = "contradiction"
else:
    # the premise gives only an estimate for the amount and time period
    # any number of roses greater than 'roses_vase_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
