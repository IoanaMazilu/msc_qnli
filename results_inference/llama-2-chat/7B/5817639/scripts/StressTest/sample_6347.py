investment_premise = 50000
investment_hypothesis = 50000

# the hypothesis talks about the amount of money invested in a business, referenced also in the premise
if investment_hypothesis <= investment_premise:
    # check if the hypothesis value contradicts the estimate of 'investment_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the amount of money invested
    # any amount of money invested greater than 'investment_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
