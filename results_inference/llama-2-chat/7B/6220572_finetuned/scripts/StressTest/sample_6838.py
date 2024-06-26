earnings_premise = 4000
earnings_hypothesis = 9000

# the hypothesis talks about the amount of earnings, referenced also in the premise
if earnings_hypothesis <= earnings_premise:
    # check if the hypothesis value contradicts the estimate of more than 'earnings_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of roses
    # any number of roses greater than 'earnings_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
