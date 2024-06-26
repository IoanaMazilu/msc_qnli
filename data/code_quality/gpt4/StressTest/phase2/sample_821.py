grapes_kg_premise = 8
grapes_kg_hypothesis = 8
mangoes_kg_premise = 9
mangoes_kg_hypothesis = 9

# the hypothesis refers to the quantities of purchased grapes and mangoes mentioned in the premise
if grapes_kg_hypothesis >= grapes_kg_premise:
    # check if the hypothesis value contradicts the assertion of less than 'grapes_kg_premise' grapes
    label = "contradiction"
elif mangoes_kg_hypothesis != mangoes_kg_premise:
    # check if the amount of purchased mangoes in the hypothesis contradicts the amount of purchased mangoes in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
