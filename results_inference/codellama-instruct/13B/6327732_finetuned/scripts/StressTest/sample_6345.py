investment_premise = 50000
investment_hypothesis = 10000

# the hypothesis refers to the investment amount mentioned in the premise
if investment_premise <= investment_hypothesis:
    # check if the estimate of 'investment_hypothesis' contradicts the investment amount in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the investment amount
    # any investment amount greater than 'investment_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
