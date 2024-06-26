business_value_premise = 14000
business_value_hypothesis = 64000

# the hypothesis refers to the value of the business mentioned in the premise
if business_value_premise >= business_value_hypothesis:
    # check if the value of the business in the premise contradicts the estimate of 'less than business_value_hypothesis'
    label = "contradiction"
else:
    # if the premise value does not contradict the hypothesis estimate, we can infer entailment
    label = "entailment"

print(label)
