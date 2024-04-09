amount_invested_premise = 20000
amount_invested_hypothesis = 20000

# the hypothesis talks about the amount invested by Rick, referenced also in the premise
if amount_invested_hypothesis <= amount_invested_premise:
    # check if the hypothesis value contradicts the estimate of the amount invested in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the amount invested
    # any amount invested greater than 'amount_invested_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
