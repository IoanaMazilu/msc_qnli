business_income_premise = 64000
business_income_hypothesis = 14000

# the hypothesis talks about the business income which is less than the premise
if business_income_hypothesis >= business_income_premise:
    # check if the hypothesis value contradicts the estimate of less than 'business_income_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the business income
    # any business income less than 'business_income_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
