business_value_premise = 14000
business_value_hypothesis = 24000

# the hypothesis refers to the value of a business mentioned in the premise
if business_value_hypothesis!= business_value_premise:
    # check if the business value in the hypothesis contradicts the business value in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise value, we can infer entailment
    label = "entailment"

print(label)
