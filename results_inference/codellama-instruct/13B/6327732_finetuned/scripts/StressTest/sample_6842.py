premise_amount = 20000
premise_duration = 6
hypothesis_amount = 20000
hypothesis_duration = 6

# the hypothesis refers to the amount invested by Rick and the duration of the investment
if hypothesis_amount <= premise_amount:
    # check if the hypothesis value contradicts the premise amount
    label = "contradiction"
elif hypothesis_duration > premise_duration:
    # check if the hypothesis duration contradicts the premise duration
    label = "contradiction"
else:
    # the premise gives only an estimate for the amount invested by Rick
    # any amount greater than 'premise_amount' and duration greater than 'premise_duration' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
