investment_premise = 10000
investment_hypothesis = 50000

# the hypothesis refers to the amount of investment mentioned in the premise
if investment_premise <= investment_hypothesis:
    # check if the estimate of 'investment_hypothesis' contradicts the amount of investment in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the amount of investment
    # any amount of investment greater than 'investment_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
