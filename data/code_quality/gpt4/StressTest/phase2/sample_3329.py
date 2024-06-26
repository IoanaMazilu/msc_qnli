interest_rate_premise = 5
interest_rate_hypothesis = 5

# the hypothesis refers to the interest rate for Rahul's loan, which is also mentioned in the premise
if interest_rate_hypothesis <= interest_rate_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
else:
    # the premise gives an exact value for the interest rate
    # any interest rate greater than 'interest_rate_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
