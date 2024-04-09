earnings_premise = 9000
earnings_hypothesis = 4000

# the hypothesis talks about the amount of money earned by the person and Rick, referenced also in the premise
if earnings_hypothesis <= earnings_premise:
    # check if the hypothesis value contradicts the estimate of 'earnings_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the amount of money earned
    # any amount of money earned greater than 'earnings_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
