earnings_premise = 210
earnings_hypothesis = 210

# the hypothesis refers to the earnings of Michael mentioned in the premise
if earnings_hypothesis <= earnings_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
else:
    # the premise gives a specific amount of earnings
    # any amount of earnings greater than 'earnings_premise' cannot be explicitly entailed from the premise, but does not contradict it either
    label = "neutral"

print(label)
