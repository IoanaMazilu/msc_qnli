premise_interest_rate = 8
hypothesis_interest_rate = 7

# the hypothesis mentions a rate of interest greater than the one mentioned in the premise
if hypothesis_interest_rate <= premise_interest_rate:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
else:
    # the premise gives an estimate for the interest rate
    # any rate of interest greater than 'premise_interest_rate' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
