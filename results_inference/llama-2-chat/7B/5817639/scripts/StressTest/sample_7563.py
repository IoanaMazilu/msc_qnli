jill_earnings_premise = 8.00
jill_earnings_hypothesis = 70

# the hypothesis talks about the tip rate of Jill, which is mentioned in the premise
if jill_earnings_hypothesis <= jill_earnings_premise:
    # check if the hypothesis value contradicts the estimate of less than 'jill_earnings_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the tip rate
    # any tip rate less than 'jill_earnings_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
