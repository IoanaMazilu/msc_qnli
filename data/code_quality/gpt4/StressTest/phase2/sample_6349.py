investment_praveen_premise = 30000
investment_praveen_hypothesis = 90000

# the hypothesis talks about the amount Mr Praveen invested in a business, referenced also in the premise
if investment_praveen_hypothesis <= investment_praveen_premise:
    # check if the hypothesis value contradicts the estimate of more than 'investment_praveen_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the investment
    # any investment amount greater than 'investment_praveen_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
