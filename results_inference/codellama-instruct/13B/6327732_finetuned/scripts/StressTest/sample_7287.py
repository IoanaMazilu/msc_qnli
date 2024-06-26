business_value_premise = 14000
business_value_hypothesis = 64000

# the hypothesis refers to the business value mentioned in the premise
if business_value_hypothesis >= business_value_premise:
    # check if the estimate of 'business_value_hypothesis' contradicts the business value in the premise
    label = "contradiction"
else:
    # the premise gives an estimate for the business value
    # any business value less than 'business_value_hypothesis' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
