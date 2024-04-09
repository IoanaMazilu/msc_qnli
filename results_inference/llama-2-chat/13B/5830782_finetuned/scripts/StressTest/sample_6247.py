investment_premise = 600000
investment_hypothesis = 100000

# the hypothesis talks about the amount of money invested by Raviraj, referenced also in the premise
if investment_hypothesis >= investment_premise:
    # check if the hypothesis value contradicts the estimate of less than 'investment_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the investment
    # any investment less than 'investment_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
