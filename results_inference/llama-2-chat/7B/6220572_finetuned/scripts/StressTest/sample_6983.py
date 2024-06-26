rate_premise = 6
rate_hypothesis = 8

# the hypothesis refers to the interest rate of borrowing money, also mentioned in the premise
if rate_hypothesis == rate_premise:
    # check if the rate in the hypothesis contradicts the rate in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the interest rate
    # any interest rate greater than 'rate_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
