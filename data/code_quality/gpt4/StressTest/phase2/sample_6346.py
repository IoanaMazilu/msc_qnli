investment_premise = 10000
investment_hypothesis = 50000

# the hypothesis makes a statement about the investment made by Mr Sharad, referenced also in the premise
if investment_hypothesis <= investment_premise:
    # check if the hypothesis value contradicts the estimate of more than 'investment_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the investment
    # any investment amount greater than 'investment_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
