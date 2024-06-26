premise_interest_rate = 8
hypothesis_interest_rate = 4

# the hypothesis talks about the interest rate mentioned in the premise
if hypothesis_interest_rate <= premise_interest_rate:
    # check if the hypothesis value contradicts the estimate of more than 'premise_interest_rate'
    label = "contradiction"
else:
    # the premise gives only an estimate for the interest rate
    # any interest rate greater than 'premise_interest_rate' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
