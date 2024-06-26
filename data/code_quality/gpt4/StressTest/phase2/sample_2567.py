grapes_kg_premise = 8
grapes_kg_hypothesis = 8
mangoes_kg_premise = 9
mangoes_kg_hypothesis = 9

# the hypothesis refers to the quantity and price of grapes and mangoes mentioned in the premise
if grapes_kg_hypothesis <= grapes_kg_premise:
    # check if the estimate of 'grapes_kg_hypothesis' contradicts the number of grapes kg in the premise
    label = "contradiction"
elif mangoes_kg_hypothesis != mangoes_kg_premise:
    # check if the number of mangoes kg in the hypothesis contradicts the number of mangoes kg reported in the premise
    label = "contradiction"
else:
    # premise gives only an estimate for the number of grapes kg
    # any number of grapes kg greater than 'grapes_kg_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
