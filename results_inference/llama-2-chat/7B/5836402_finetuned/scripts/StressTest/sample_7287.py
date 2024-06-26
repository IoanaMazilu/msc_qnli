business_value_premise = 14000
business_value_hypothesis = 64000

# the hypothesis talks about the value of a business, which is also referenced in the premise
if business_value_hypothesis >= business_value_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
else:
    # the premise gives only an estimate for the business value
    # any value less than 'business_value_hypothesis' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
