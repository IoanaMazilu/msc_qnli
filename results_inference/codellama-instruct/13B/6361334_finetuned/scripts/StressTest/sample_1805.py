interest_rate_premise = 8
interest_rate_hypothesis = 4

# the hypothesis refers to the interest rate mentioned in the premise
if interest_rate_hypothesis <= interest_rate_premise:
    # check if the estimate of 'interest_rate_hypothesis' contradicts the interest rate in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the interest rate
    # any interest rate greater than 'interest_rate_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
