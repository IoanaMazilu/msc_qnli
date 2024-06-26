business_investment_premise = 50000
business_investment_hypothesis = 10000

# the hypothesis refers to the amount of investment mentioned in the premise
if business_investment_premise <= business_investment_hypothesis:
    # check if the estimate of 'business_investment_hypothesis' contradicts the amount of investment in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the amount of investment
    # any amount of investment greater than 'business_investment_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
