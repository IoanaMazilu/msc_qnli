premise_interest_rate = 8
hypothesis_interest_rate = 7

# the hypothesis mentions a rate higher than the premise rate
if hypothesis_interest_rate > premise_interest_rate:
    # check if the hypothesis value contradicts the premise rate
    label = "contradiction"
else:
    # the premise gives an estimate for the interest rate
    # any rate higher than 'premise_interest_rate' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
