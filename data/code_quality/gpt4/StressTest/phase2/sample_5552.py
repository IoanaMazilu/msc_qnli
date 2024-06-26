grapes_kg_premise = 6
grapes_kg_hypothesis = 8
grapes_rate_premise = 74
grapes_rate_hypothesis = 74
mangoes_kg_premise = 9
mangoes_kg_hypothesis = 9
mangoes_rate_premise = 59
mangoes_rate_hypothesis = 59

# the hypothesis refers to the amount and rate of purchased grapes and mangoes mentioned in the premise
if grapes_kg_hypothesis != grapes_kg_premise:
    # check if the amount of grapes in the hypothesis contradicts the amount in the premise
    label = "contradiction"
elif grapes_rate_hypothesis != grapes_rate_premise:
    # check if the rate of grapes in the hypothesis contradicts the rate in the premise
    label = "contradiction"
elif mangoes_kg_hypothesis != mangoes_kg_premise:
    # check if the amount of mangoes in the hypothesis contradicts the amount in the premise
    label = "contradiction"
elif mangoes_rate_hypothesis != mangoes_rate_premise:
    # check if the rate of mangoes in the hypothesis contradicts the rate in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
