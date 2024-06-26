investment_premise = 2
investment_hypothesis = 3

# the hypothesis refers to the number of times the investment is returned, referenced also in the premise
if investment_hypothesis >= investment_premise:
    # check if the hypothesis value contradicts the estimate of 'investment_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of times the investment is returned
    # any number of times less than 'investment_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
