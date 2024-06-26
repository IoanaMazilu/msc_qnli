grapes_kg_premise = 5
grapes_kg_hypothesis = 8
rate_grapes = 70
mangoes_kg_premise = 9
mangoes_kg_hypothesis = 9
rate_mangoes = 55

# the hypothesis refers to the amount and price of grapes and mangoes mentioned in the premise
if grapes_kg_hypothesis <= grapes_kg_premise:
    # check if the hypothesis value contradicts the estimate of more than 'grapes_kg_premise' kgs of grapes
    label = "contradiction"
elif mangoes_kg_hypothesis != mangoes_kg_premise:
    # check if the number of kgs of mangoes in the hypothesis contradicts the number of kgs of mangoes reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the amount of grapes
    # the number 'grapes_kg_hypothesis' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
