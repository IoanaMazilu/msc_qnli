interest_rate_premise = 4
interest_rate_hypothesis = 5

# the hypothesis refers to an interest rate that Rahul borrowed at, referenced also in the premise
if interest_rate_hypothesis <= interest_rate_premise:
    # check if the interest rate in the hypothesis contradicts the premise estimate of more than 'interest_rate_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the interest rate
    # any interest rate greater than 'interest_rate_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
