money_premise = 95
money_hypothesis = 95

# the hypothesis refers to the amount of money given to John mentioned in the premise
if money_hypothesis >= money_premise:
    # check if the estimate of'money_hypothesis' contradicts the amount of money in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
