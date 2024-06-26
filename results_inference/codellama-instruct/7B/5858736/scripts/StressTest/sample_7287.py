premise_business_value = 14000
hypothesis_business_value = 64000

# the hypothesis refers to the value of the business mentioned in the premise
if premise_business_value <= hypothesis_business_value:
    # check if the estimate of 'hypothesis_business_value' contradicts the value of the business in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise value, we can infer entailment
    label = "entailment"

print(label)
