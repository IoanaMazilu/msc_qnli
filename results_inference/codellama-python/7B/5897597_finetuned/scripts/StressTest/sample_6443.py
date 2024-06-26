grapes_kg_premise = 7
grapes_kg_hypothesis = 7
grapes_rate_premise = 68
grapes_rate_hypothesis = 68
mangoes_kg_premise = 9
mangoes_kg_hypothesis = 9
mangoes_rate_premise = 48
mangoes_rate_hypothesis = 48

# the hypothesis refers to the quantity and rate of grapes and mangoes purchased by Andrew mentioned in the premise
if grapes_kg_hypothesis >= grapes_kg_premise:
    # check if the hypothesis value contradicts the premise value of 'grapes_kg_premise'
    label = "contradiction"
elif grapes_rate_hypothesis!= grapes_rate_premise:
    # check if the rate of grapes in the hypothesis contradicts the rate of grapes reported in the premise
    label = "contradiction"
elif mangoes_kg_hypothesis!= mangoes_kg_premise:
    # check if the quantity of mangoes in the hypothesis contradicts the quantity of mangoes reported in the premise
    label = "contradiction"
elif mangoes_rate_hypothesis!= mangoes_rate_premise:
    # check if the rate of mangoes in the hypothesis contradicts the rate of mangoes reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)