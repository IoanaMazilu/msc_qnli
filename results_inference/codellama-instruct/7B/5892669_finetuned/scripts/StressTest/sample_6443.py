grapes_kg_premise = 7
grapes_kg_hypothesis = 7
mangoes_kg_premise = 9
mangoes_kg_hypothesis = 9

# the hypothesis refers to the weight of grapes and mangoes purchased by Andrew mentioned in the premise
if grapes_kg_hypothesis >= grapes_kg_premise:
    # check if the weight of 'grapes_kg_hypothesis' contradicts the weight of grapes in the premise
    label = "contradiction"
elif mangoes_kg_hypothesis!= mangoes_kg_premise:
    # check if the weight of mangoes in the hypothesis contradicts the weight of mangoes reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
