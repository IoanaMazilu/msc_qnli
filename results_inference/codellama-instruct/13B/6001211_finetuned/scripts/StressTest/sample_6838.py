earnings_premise = 4000
earnings_hypothesis = 9000

# the hypothesis refers to the total earnings mentioned in the premise
if earnings_hypothesis <= earnings_premise:
    # check if the value in the hypothesis contradicts the estimate of more than 'earnings_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the earnings
    # any amount greater than 'earnings_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
