earnings_premise = 810
earnings_hypothesis = 210

# the hypothesis talks about Michael's earnings, referenced also in the premise
if earnings_hypothesis >= earnings_premise:
    # check if the hypothesis value contradicts the estimate of less than 'earnings_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the earnings
    # any earnings less than 'earnings_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
