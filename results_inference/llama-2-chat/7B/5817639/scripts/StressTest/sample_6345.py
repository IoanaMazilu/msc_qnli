business_investment_premise = 50000
business_investment_hypothesis = 10000

# the hypothesis talks about a higher amount of investment compared to the premise
if business_investment_hypothesis <= business_investment_premise:
    # check if the hypothesis value contradicts the estimate of the investment in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the investment
    # any amount of investment greater than 'business_investment_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
