profit_premise = 22000
profit_hypothesis = 42000

# the hypothesis refers to the profit in the business at the end of the year, which is also mentioned in the premise
if profit_premise >= profit_hypothesis:
    # check if the profit in the premise contradicts the hypothesis
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise, we can infer entailment
    label = "entailment"

print(label)
