profit_premise = 22000
profit_hypothesis = 22000

# the hypothesis refers to the profit in the business at the end of the year mentioned in the premise
if profit_hypothesis <= profit_premise:
    # check if the hypothesis value contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise, we can infer entailment
    label = "entailment"

print(label)
