business_value_premise = 14000
business_value_hypothesis = 64000

# the hypothesis refers to the business value mentioned in the premise
if business_value_premise >= business_value_hypothesis:
    # check if the business value in the premise contradicts the estimate of less than 'business_value_hypothesis'
    label = "contradiction"
else:
    # if the business value in the premise does not contradict the estimate in the hypothesis, we can infer entailment
    label = "entailment"

print(label)
# 