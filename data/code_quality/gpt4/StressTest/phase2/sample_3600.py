interest_rate_premise = 4
interest_rate_hypothesis = 8

# the hypothesis discusses the same topic as the premise but alters the interest rate 
if interest_rate_premise >= interest_rate_hypothesis:
    # check if the interest rate in the premise contradicts the estimate of less than 'interest_rate_hypothesis'
    label = "contradiction"
else:
    # the premise gives only one exact value for the interest rate
    # any interest rate less than 'interest_rate_hypothesis' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
