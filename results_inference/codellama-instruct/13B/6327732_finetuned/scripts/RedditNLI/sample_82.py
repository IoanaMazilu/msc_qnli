investment_premise = 1000000000
investment_hypothesis = 1000000000

# the hypothesis and premise mention the amount of investment in US dollars
if investment_premise!= investment_hypothesis:
    # check if the amount of investment in the hypothesis contradicts the amount of investment in the premise
    label = "contradiction"
else:
    # the premise gives an exact amount of investment
    # any amount of investment in the hypothesis equal to or greater than the premise amount is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
