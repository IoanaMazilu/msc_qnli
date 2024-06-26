profit_premise = 22000
profit_hypothesis = 22000

# the hypothesis refers to the profit mentioned in the premise
if profit_hypothesis!= profit_premise:
    # check if the profit in the hypothesis contradicts the profit in the premise
    label = "contradiction"
else:
    # if the profit in the hypothesis does not contradict the profit in the premise, we can infer entailment
    label = "entailment"

print(label)
