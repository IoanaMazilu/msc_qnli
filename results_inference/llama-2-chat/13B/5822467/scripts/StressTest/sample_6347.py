investment_premise = 50000
investment_hypothesis = 30000

# the hypothesis refers to the amount of investment mentioned in the premise
if investment_premise <= investment_hypothesis:
    # check if the hypothesis value contradicts the amount of investment in the premise
    label = "contradiction"
elif investment_hypothesis == 0:
    # check if the hypothesis value is consistent with the premise
    label = "neutral"
else:
    # the premise gives an exact amount of investment
    # any amount of investment less than 'investment_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
