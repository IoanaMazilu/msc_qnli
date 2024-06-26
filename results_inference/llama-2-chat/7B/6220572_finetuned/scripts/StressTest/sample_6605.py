investment_return_premise = 2
investment_return_hypothesis = 2

# the hypothesis refers to the number of times the investment will be returned, mentioned in the premise
if investment_return_hypothesis >= investment_return_premise:
    # check if the estimate of 'investment_return_hypothesis' contradicts the number of times the investment will be returned in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of times the investment will be returned
    # any number of times less than 'investment_return_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
