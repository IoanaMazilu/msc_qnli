premise_amount = 1300
hypothesis_amount = 4300

# the hypothesis talks about the amount of Deepak's share
if hypothesis_amount <= premise_amount:
    # check if the hypothesis value contradicts the estimate of 'premise_amount'
    label = "contradiction"
else:
    # the premise gives only an estimate for the amount of Deepak's share
    # any amount less than 4300 is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
