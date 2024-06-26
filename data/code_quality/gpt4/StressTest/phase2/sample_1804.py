interest_rate_premise = 5
interest_rate_hypothesis = 8

# the hypothesis talks about the interest rate, which is also mentioned in the premise
if interest_rate_hypothesis <= interest_rate_premise:
    # check if the hypothesis value contradicts the premise's estimate of more than 'interest_rate_premise'
    label = "contradiction"
else:
    # the premise only gives an estimate for the interest rate
    # any interest rate greater than 'interest_rate_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
