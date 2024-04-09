jill_earnings_premise = 4.00
jill_earnings_hypothesis = 4.00
tip_rate_premise = 0.15
tip_rate_hypothesis = 0.45

# the hypothesis talks about the tip rate, which is also mentioned in the premise
if jill_earnings_hypothesis <= jill_earnings_premise:
    # check if the hypothesis value contradicts the estimate of the hourly wage in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the hourly wage, and any value greater than $4.00 is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
