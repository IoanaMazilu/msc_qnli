profit_premise = 22000
profit_hypothesis = 22000

# the hypothesis refers to the profit mentioned in the premise
if profit_hypothesis <= profit_premise:
    # check if the hypothesis value contradicts the profit in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
