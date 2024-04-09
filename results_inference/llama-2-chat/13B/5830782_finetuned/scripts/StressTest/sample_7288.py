business_value_premise = 64000
business_value_hypothesis = 14000

# the hypothesis talks about the value of a business, referenced also in the premise
if business_value_hypothesis >= business_value_premise:
    # check if the hypothesis value contradicts the estimate of less than 'business_value_premise'
    label = "contradiction"
elif business_value_hypothesis < business_value_premise:
    # the premise gives only an estimate for the business value
    # any business value less than 'business_value_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
