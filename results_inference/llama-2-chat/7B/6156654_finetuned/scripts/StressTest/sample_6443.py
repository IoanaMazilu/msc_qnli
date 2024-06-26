grapes_purchased_premise = 7
grapes_purchased_hypothesis = 7
mangoes_purchased_premise = 9
mangoes_purchased_hypothesis = 9
rate_grapes_premise = 68
rate_grapes_hypothesis = 68
rate_mangoes_premise = 48
rate_mangoes_hypothesis = 48

# the hypothesis refers to the same quantities as the premise, but with different values
if grapes_purchased_hypothesis >= grapes_purchased_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
elif mangoes_purchased_hypothesis!= mangoes_purchased_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
