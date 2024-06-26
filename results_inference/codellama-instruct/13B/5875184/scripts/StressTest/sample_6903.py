premise_total = 160
hypothesis_total = 360

# the hypothesis talks about the total amount paid for renting the tool
if premise_total <= hypothesis_total:
    # check if the hypothesis value contradicts the estimate of 'premise_total'
    label = "contradiction"
else:
    # the premise gives only an estimate for the total amount paid
    # any amount greater than 'premise_total' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
