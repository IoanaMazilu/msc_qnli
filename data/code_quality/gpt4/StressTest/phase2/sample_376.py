interest_rate_premise = 3
interest_rate_hypothesis = 6

# the hypothesis gives a specific interest rate, while the premise only sets a lower limit
if interest_rate_hypothesis <= interest_rate_premise:
    # check if the hypothesis value contradicts the premise's estimate of more than 'interest_rate_premise'
    label = "contradiction"
else:
    # the premise gives only a lower limit for the interest rate
    # any interest rate greater than 'interest_rate_premise' is consistent with the premise, but cannot be explicitly entailed from the premise 
    label = "neutral"

print(label)
