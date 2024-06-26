grapes_kg_premise = 7
grapes_kg_hypothesis = 1
grapes_rate_premise = 68
grapes_rate_hypothesis = 68
mangoes_kg_premise = 9
mangoes_kg_hypothesis = 9
mangoes_rate_premise = 48
mangoes_rate_hypothesis = 48

# the hypothesis refers to the number of kg of grapes and mangoes and their rates mentioned in the premise
if grapes_kg_premise <= grapes_kg_hypothesis:
    # check if the estimate of 'grapes_kg_hypothesis' contradicts the number of kg of grapes in the premise
    label = "contradiction"
elif grapes_rate_hypothesis!= grapes_rate_premise:
    # check if the rate of grapes in the hypothesis contradicts the rate of grapes reported in the premise
    label = "contradiction"
elif mangoes_kg_hypothesis!= mangoes_kg_premise:
    # check if the number of kg of mangoes in the hypothesis contradicts the number of kg of mangoes reported in the premise
    label = "contradiction"
elif mangoes_rate_hypothesis!= mangoes_rate_premise:
    # check if the rate of mangoes in the hypothesis contradicts the rate of mangoes reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
