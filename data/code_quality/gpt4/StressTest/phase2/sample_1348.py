business_investment_premise = 75000
business_investment_hypothesis = 25000

# the hypothesis provides a specific value about the business investment made in 1996, also mentioned in the premise
if business_investment_hypothesis >= business_investment_premise:
    # check if the hypothesis value contradicts the estimate of less than 'business_investment_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the business investment
    # any investment less than 'business_investment_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
