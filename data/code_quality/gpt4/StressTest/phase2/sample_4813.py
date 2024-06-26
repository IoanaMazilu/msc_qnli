earnings_rise_premise = 66
earnings_rise_hypothesis = 36

# The hypothesis talks about the percentage increase in Albert's earnings
if earnings_rise_hypothesis >= earnings_rise_premise:
    # check if the hypothesis value contradicts the estimate of less than 'earnings_rise_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the increase in earnings
    # any percentage increase less than 'earnings_rise_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
