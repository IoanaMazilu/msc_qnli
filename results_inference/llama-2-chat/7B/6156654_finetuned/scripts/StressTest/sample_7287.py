business_value_premise = 14000
business_value_hypothesis = 64000

# the hypothesis refers to the business value, which is also mentioned in the premise
if business_value_premise < business_value_hypothesis:
    # check if the business value in the premise contradicts the hypothesis
    label = "contradiction"
else:
    # if the business value in the premise is equal to or greater than the hypothesis, we can infer entailment
    label = "entailment"

print(label)
