interest_rate_premise = 8
interest_rate_hypothesis = 4

# the hypothesis refers to the interest rate mentioned in the premise
if interest_rate_hypothesis >= interest_rate_premise:
    # check if the interest rate in the hypothesis contradicts the estimate of less than 'interest_rate_premise'
    label = "contradiction"
elif interest_rate_hypothesis > 0:
    # if the interest rate in the hypothesis is greater than 0 and less than 'interest_rate_premise',
    # it does not contradict the premise but cannot be explicitly entailed from the premise
    label = "neutral"
else:
    # if the interest rate in the hypothesis is 0,
    # it contradicts the premise as it cannot double the investment
    label = "contradiction"

print(label)
