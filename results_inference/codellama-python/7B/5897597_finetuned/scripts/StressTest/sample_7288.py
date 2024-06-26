business_value_premise = 64000
business_value_hypothesis = 14000

# the hypothesis refers to the value of the business mentioned in the premise
if business_value_hypothesis >= business_value_premise:
    # check if the value of 'business_value_hypothesis' contradicts the estimate of less than 'business_value_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the business value
    # any value less than 'business_value_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
