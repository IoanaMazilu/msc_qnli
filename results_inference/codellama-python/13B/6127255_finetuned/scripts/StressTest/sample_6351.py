profit_premise = 22000
profit_hypothesis = 42000

# the hypothesis refers to the profit in the business mentioned in the premise
if profit_premise >= profit_hypothesis:
    # check if the profit in the premise contradicts the estimate of less than 'profit_hypothesis'
    label = "contradiction"
elif profit_premise < profit_hypothesis:
    # check if the profit in the premise is less than 'profit_hypothesis'
    label = "entailment"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer neutrality
    label = "neutral"

print(label)
