business_investment_premise = 10000
business_investment_hypothesis = 50000

# the hypothesis talks about the amount Mr Sharad invested in the business, referenced also in the premise
if business_investment_hypothesis <= business_investment_premise:
    # check if the hypothesis value contradicts the estimate of more than 'business_investment_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the business investment
    # any investment greater than 'business_investment_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
