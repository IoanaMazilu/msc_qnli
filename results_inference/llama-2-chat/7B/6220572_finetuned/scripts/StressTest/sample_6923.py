earnings_premise = 210
earnings_hypothesis = 210

# the hypothesis refers to the number of hours worked by Michael, also mentioned in the premise
if earnings_hypothesis == earnings_premise:
    # check if the hypothesis value contradicts the estimate of 'earnings_premise'
    label = "contradiction"
else:
    # the premise gives an exact number for the earnings
    # any number of hours consistent with the premise is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
