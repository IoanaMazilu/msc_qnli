grapes_kg_premise = 6
grapes_kg_hypothesis = 7
rate_grapes = 74
mangoes_kg_premise = 9
mangoes_kg_hypothesis = 9
rate_mangoes = 59

# the hypothesis refers to the weight and rate of grapes and mangoes purchased by Andrew mentioned in the premise
if grapes_kg_hypothesis <= grapes_kg_premise:
    # check if the weight of grapes in the hypothesis contradicts the weight of grapes in the premise
    label = "contradiction"
elif mangoes_kg_hypothesis != mangoes_kg_premise:
    # check if the weight of mangoes in the hypothesis contradicts the weight of mangoes in the premise
    label = "contradiction"
elif rate_grapes != 74 or rate_mangoes != 59:
    # check if the rate of grapes or mangoes in the hypothesis contradicts the rate in the premise
    label = "contradiction"
else:
    # if the weights and rates in the hypothesis do not contradict the ones in the premise, we can infer entailment
    label = "entailment"

print(label)
