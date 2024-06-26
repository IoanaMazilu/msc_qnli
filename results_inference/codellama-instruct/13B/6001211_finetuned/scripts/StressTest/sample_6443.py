grapes_kg_premise = 7
grapes_kg_hypothesis = 7
mangoes_kg_premise = 9
mangoes_kg_hypothesis = 9

# the hypothesis refers to the quantity of grapes and mangoes purchased, mentioned in the premise
if grapes_kg_hypothesis >= grapes_kg_premise:
    # check if the hypothesis value contradicts the premise value of 'grapes_kg_premise'
    label = "contradiction"
elif mangoes_kg_hypothesis!= mangoes_kg_premise:
    # check if the hypothesis value contradicts the premise value of'mangoes_kg_premise'
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
