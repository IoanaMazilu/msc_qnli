grapes_kg_premise = 1
grapes_kg_hypothesis = 7
rate_grapes_premise = 68
rate_grapes_hypothesis = 68
mangoes_kg_premise = 9
mangoes_kg_hypothesis = 9
rate_mangoes_premise = 48
rate_mangoes_hypothesis = 48

# the hypothesis talks about the quantity and rate of purchased grapes and mangoes, which are also referenced in the premise
if grapes_kg_hypothesis <= grapes_kg_premise:
    # check if the hypothesis value contradicts the estimate of more than 'grapes_kg_premise' kg of grapes
    label = "contradiction"
elif rate_grapes_hypothesis!= rate_grapes_premise:
    # check if the rate of grapes in the hypothesis contradicts the rate of grapes reported in the premise
    label = "contradiction"
elif mangoes_kg_hypothesis!= mangoes_kg_premise:
    # check if the quantity of purchased mangoes in the hypothesis contradicts the quantity of purchased mangoes reported in the premise
    label = "contradiction"
elif rate_mangoes_hypothesis!= rate_mangoes_premise:
    # check if the rate of mangoes in the hypothesis contradicts the rate of mangoes reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the quantity of purchased grapes
    # any quantity of grapes greater than 'grapes_kg_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
