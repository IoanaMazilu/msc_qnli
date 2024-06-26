grapes_kg_premise = 7
grapes_kg_hypothesis = 7
mangoes_kg_premise = 9
mangoes_kg_hypothesis = 9

# the hypothesis refers to the amount of grapes and mangoes purchased by Andrew mentioned in the premise
if grapes_kg_hypothesis >= grapes_kg_premise:
    # check if the hypothesis value contradicts the premise of purchasing less than 'grapes_kg_premise' grapes
    label = "contradiction"
elif mangoes_kg_hypothesis!= mangoes_kg_premise:
    # check if the amount of mangoes purchased in the hypothesis contradicts the amount of mangoes purchased in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
