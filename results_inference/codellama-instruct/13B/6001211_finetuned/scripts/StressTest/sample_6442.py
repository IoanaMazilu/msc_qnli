grapes_kg_premise = 1
grapes_kg_hypothesis = 7
grape_rate_premise = 68
grape_rate_hypothesis = 68
mangoes_kg_premise = 9
mangoes_kg_hypothesis = 9
mango_rate_premise = 48
mango_rate_hypothesis = 48

# the hypothesis refers to the number of kg of grapes and mangoes purchased and the rate per kg, mentioned in the premise
if grapes_kg_hypothesis <= grapes_kg_premise:
    # check if the hypothesis value contradicts the estimate of more than 'grapes_kg_premise'
    label = "contradiction"
elif grape_rate_hypothesis!= grape_rate_premise:
    # check if the rate per kg for grapes in the hypothesis contradicts the rate per kg for grapes reported in the premise
    label = "contradiction"
elif mangoes_kg_hypothesis!= mangoes_kg_premise:
    # check if the number of kg of mangoes in the hypothesis contradicts the number of kg of mangoes reported in the premise
    label = "contradiction"
elif mango_rate_hypothesis!= mango_rate_premise:
    # check if the rate per kg for mangoes in the hypothesis contradicts the rate per kg for mangoes reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of kg of grapes
    # any number of kg of grapes greater than 'grapes_kg_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
