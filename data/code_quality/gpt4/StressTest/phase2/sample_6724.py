amount_premise = 1600
amount_hypothesis = 3600
interest_rate_premise = 6
interest_rate_hypothesis = 6

# the hypothesis refers to the amount and interest rate mentioned in the premise
if amount_hypothesis <= amount_premise:
    # check if the amount in the hypothesis contradicts the estimate of more than 'amount_premise'
    label = "contradiction"
elif interest_rate_hypothesis != interest_rate_premise:
    # check if the interest rate in the hypothesis contradicts the interest rate mentioned in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the amount
    # any amount greater than 'amount_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
