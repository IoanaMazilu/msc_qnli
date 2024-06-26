grapes_kg_premise = 1
grapes_kg_hypothesis = 7
grapes_rate_premise = 68
grapes_rate_hypothesis = 68
mangoes_kg_premise = 9
mangoes_kg_hypothesis = 9
mangoes_rate_premise = 48
mangoes_rate_hypothesis = 48

# the hypothesis talks about the quantity and rate of grapes and mangoes purchased by Andrew, which is also mentioned in the premise
if grapes_kg_hypothesis <= grapes_kg_premise:
    # check if the hypothesis value contradicts the estimate of more than 'grapes_kg_premise'
    label = "contradiction"
elif grapes_rate_hypothesis!= grapes_rate_premise or mangoes_rate_hypothesis!= mangoes_rate_premise:
    # check if the rate of grapes or mangoes in the hypothesis contradicts the rate mentioned in the premise
    label = "contradiction"
elif mangoes_kg_hypothesis!= mangoes_kg_premise:
    # check if the quantity of mangoes in the hypothesis contradicts the quantity mentioned in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the quantity of grapes
    # any quantity of grapes greater than 'grapes_kg_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
