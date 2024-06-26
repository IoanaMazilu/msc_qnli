dollar_per_hour_premise = 0
dollar_per_hour_hypothesis = 0

# the hypothesis talks about the pay rate for James, referenced also in the premise
if dollar_per_hour_hypothesis <= dollar_per_hour_premise:
    # check if the hypothesis value contradicts the estimate of the pay rate in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the pay rate
    # any pay rate greater than 'dollar_per_hour_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
