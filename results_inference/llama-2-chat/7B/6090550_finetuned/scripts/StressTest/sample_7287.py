 business_value_premise = 14000
business_value_hypothesis = 64000

# the hypothesis talks about the value of a business, which is also mentioned in the premise
if business_value_premise > business_value_hypothesis:
    # check if the value of the business in the premise contradicts the value in the hypothesis
    label = "contradiction"
elif business_value_premise == business_value_hypothesis:
    # check if the value of the business in the premise is equal to the value in the hypothesis
    label = "neutral"
else:
    # if the value of the business in the premise is less than the value in the hypothesis, we can infer entailment
    label = "entailment"

print(label)
