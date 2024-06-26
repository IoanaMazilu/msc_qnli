investment_premise = 50000
investment_hypothesis = 50000

# the hypothesis talks about the amount of money Mr Sharad invested, referenced also in the premise
if investment_hypothesis >= investment_premise:
    # check if the hypothesis value contradicts the estimate of less than 'investment_premise'
    label = "contradiction"
else:
    # the premise gives an exact amount for the investment
    # any amount less than 'investment_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
