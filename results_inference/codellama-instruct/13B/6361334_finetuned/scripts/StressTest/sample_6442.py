grapes_kg_premise = 1
grapes_kg_hypothesis = 7
mangoes_kg_premise = 9
mangoes_kg_hypothesis = 9

# the hypothesis refers to the number of kg of grapes and mangoes mentioned in the premise
if grapes_kg_hypothesis <= grapes_kg_premise:
    # check if the estimate of 'grapes_kg_hypothesis' contradicts the number of kg of grapes in the premise
    label = "contradiction"
elif mangoes_kg_hypothesis!= mangoes_kg_premise:
    # check if the number of kg of mangoes in the hypothesis contradicts the number of kg of mangoes reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
