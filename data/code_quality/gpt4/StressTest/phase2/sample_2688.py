amount_premise = 3450
interest_rate_premise = 6
amount_hypothesis = 7450
interest_rate_hypothesis = 6

# the hypothesis refers to the amount received from Anwar and the interest rate, which are also mentioned in the premise
if amount_hypothesis <= amount_premise:
    # check if the estimate of 'amount_hypothesis' contradicts the amount received from Anwar in the premise
    label = "contradiction"
elif interest_rate_hypothesis != interest_rate_premise:
    # check if the interest rate in the hypothesis contradicts the interest rate mentioned in the premise
    label = "contradiction"
else:
    # the premise gives an exact amount and interest rate
    # any amount less than 'amount_hypothesis' and the same interest rate is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
