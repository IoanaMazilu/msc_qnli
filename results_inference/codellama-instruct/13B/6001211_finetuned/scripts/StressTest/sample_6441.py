grapes_kg_premise = 7
grapes_kg_hypothesis = 1
rate_grapes_premise = 68
rate_grapes_hypothesis = 68
mangoes_kg_premise = 9
mangoes_kg_hypothesis = 9
rate_mangoes_premise = 48
rate_mangoes_hypothesis = 48

# the hypothesis refers to the quantity and rate of purchased grapes and mangoes mentioned in the premise
if grapes_kg_premise <= grapes_kg_hypothesis:
    # check if the estimate of 'grapes_kg_hypothesis' contradicts the quantity of grapes in the premise
    label = "contradiction"
elif rate_grapes_premise!= rate_grapes_hypothesis:
    # check if the rate of grapes in the hypothesis contradicts the rate of grapes reported in the premise
    label = "contradiction"
elif mangoes_kg_premise!= mangoes_kg_hypothesis:
    # check if the quantity of mangoes in the hypothesis contradicts the quantity of mangoes reported in the premise
    label = "contradiction"
elif rate_mangoes_premise!= rate_mangoes_hypothesis:
    # check if the rate of mangoes in the hypothesis contradicts the rate of mangoes reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
