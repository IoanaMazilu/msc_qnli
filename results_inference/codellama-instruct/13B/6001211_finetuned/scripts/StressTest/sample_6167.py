money_to_give_premise = 95
money_to_give_hypothesis = 95

# the hypothesis refers to the amount of money given to John mentioned in the premise
if money_to_give_hypothesis >= money_to_give_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
