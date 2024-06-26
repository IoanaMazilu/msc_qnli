earnings_premise = 210
earnings_hypothesis = 210

# the hypothesis refers to the earnings of Michael mentioned in the premise
if earnings_hypothesis <= earnings_premise:
    # check if the hypothesis value contradicts the premise
    label = "contradiction"
else:
    # the premise gives a specific amount for the earnings
    # any earnings greater than 'earnings_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
