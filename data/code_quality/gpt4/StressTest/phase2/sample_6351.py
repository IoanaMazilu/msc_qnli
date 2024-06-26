profit_premise = 22000
profit_hypothesis = 42000

# the hypothesis refers to the profit in the business at the end of the year mentioned in the premise
if profit_premise >= profit_hypothesis:
    # check if the profit in the premise contradicts the estimate of less than 'profit_hypothesis'
    label = "contradiction"
elif profit_premise < profit_hypothesis:
    # if the profit in the premise is less than the profit estimate in the hypothesis, we can infer entailment
    label = "entailment"

print(label)
