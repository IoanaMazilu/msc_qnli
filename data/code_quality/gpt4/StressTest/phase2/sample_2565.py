grapes_kg_premise = 8
grapes_kg_hypothesis = 3
grapes_rate = 70
mangoes_kg_premise = 9
mangoes_kg_hypothesis = 9
mangoes_rate = 55

# the hypothesis refers to the amount of grapes and mangoes purchased by John, also mentioned in the premise
if grapes_kg_premise <= grapes_kg_hypothesis:
    # check if the estimate of 'grapes_kg_hypothesis' contradicts the amount of grapes in the premise
    label = "contradiction"
elif mangoes_kg_hypothesis != mangoes_kg_premise:
    # check if the amount of mangoes in the hypothesis contradicts the amount of mangoes reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
