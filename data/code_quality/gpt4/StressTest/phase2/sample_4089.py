grapes_kg_premise = 8
grapes_kg_hypothesis = 5
mangoes_kg_premise = 9
mangoes_kg_hypothesis = 9
rate_grapes = 70
rate_mangoes = 55

# the hypothesis refers to the amount of grapes and mangoes purchased, as mentioned in the premise
if grapes_kg_premise <= grapes_kg_hypothesis:
    # check if the estimate of 'grapes_kg_hypothesis' contradicts the amount of grapes in the premise
    label = "contradiction"
elif mangoes_kg_hypothesis != mangoes_kg_premise:
    # check if the amount of mangoes in the hypothesis contradicts the amount of mangoes reported in the premise
    label = "contradiction"
elif rate_grapes != 70 or rate_mangoes != 55:
    # check if the rate of grapes and mangoes in the hypothesis contradicts the rate reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
