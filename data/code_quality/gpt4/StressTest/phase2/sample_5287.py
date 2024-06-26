grapes_kg_premise = 2
grapes_kg_hypothesis = 8
grapes_rate_premise = 70
grapes_rate_hypothesis = 70
mangoes_kg_premise = 9
mangoes_kg_hypothesis = 9
mangoes_rate_premise = 55
mangoes_rate_hypothesis = 55

# the hypothesis refers to the quantity and rate of grapes and mangoes purchased, mentioned in the premise
if grapes_kg_hypothesis <= grapes_kg_premise:
    # check if the hypothesis value contradicts the estimate of more than 'grapes_kg_premise'
    label = "contradiction"
elif grapes_rate_hypothesis != grapes_rate_premise or mangoes_rate_hypothesis != mangoes_rate_premise:
    # check if the rates for grapes or mangoes in the hypothesis contradict the rates given in the premise
    label = "contradiction"
elif mangoes_kg_hypothesis != mangoes_kg_premise:
    # check if the quantity of mangoes in the hypothesis contradicts the quantity given in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the quantity of grapes
    # any quantity of grapes greater than 'grapes_kg_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
