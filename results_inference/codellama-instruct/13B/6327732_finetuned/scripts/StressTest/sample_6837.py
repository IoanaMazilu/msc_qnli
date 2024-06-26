earnings_premise = 9000
earnings_hypothesis = 4000

# the hypothesis refers to the number of earnings mentioned in the premise
if earnings_premise <= earnings_hypothesis:
    # check if the estimate of 'earnings_hypothesis' contradicts the number of earnings in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of earnings
    # any number of earnings greater than 'earnings_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
