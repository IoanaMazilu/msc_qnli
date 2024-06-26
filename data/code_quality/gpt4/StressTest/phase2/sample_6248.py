amount_invested_premise = 100000
amount_invested_hypothesis = 100000

# the hypothesis refers to the same investment mentioned in the premise
if amount_invested_hypothesis >= amount_invested_premise:
    # check if the hypothesis value contradicts the reported amount of investment in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
