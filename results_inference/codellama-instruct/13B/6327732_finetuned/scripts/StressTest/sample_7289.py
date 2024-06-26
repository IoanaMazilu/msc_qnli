business_value_premise = 14000
business_value_hypothesis = 24000

# the hypothesis refers to the value of the business jointly owned by the three persons
if business_value_hypothesis <= business_value_premise:
    # check if the estimate of 'business_value_hypothesis' contradicts the value of the business in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the value of the business
    # any value greater than 'business_value_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
