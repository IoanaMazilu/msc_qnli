investment_premise = 30000
investment_hypothesis = 90000

# the hypothesis refers to the amount of investment made by Mr. Praveen
if investment_premise <= investment_hypothesis:
    # check if the estimate of 'investment_hypothesis' contradicts the amount of investment in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the amount of investment
    # any amount of investment greater than 'investment_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
