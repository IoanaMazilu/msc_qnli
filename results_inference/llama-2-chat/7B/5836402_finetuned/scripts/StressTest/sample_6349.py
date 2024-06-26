investment_premise = 30000
investment_hypothesis = 90000

# the hypothesis refers to the amount of investment by Mr. Praveen mentioned in the premise
if investment_hypothesis <= investment_premise:
    # check if the hypothesis value contradicts the estimate of more than 'investment_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the investment
    # any amount of investment greater than 'investment_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)