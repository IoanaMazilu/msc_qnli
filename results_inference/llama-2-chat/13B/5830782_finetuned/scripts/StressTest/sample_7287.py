business_investment_premise = 14000
business_investment_hypothesis = 64000

# the hypothesis refers to the business investment mentioned in the premise
if business_investment_premise >= business_investment_hypothesis:
    # check if the estimate of 'business_investment_premise' contradicts the business investment in the hypothesis
    label = "contradiction"
else:
    # if the business investment in the premise does not contradict the hypothesis, we can infer entailment
    label = "entailment"

print(label)
