grapes_kg_premise = 1
grapes_kg_hypothesis = 7
mangoes_kg_premise = 9
mangoes_kg_hypothesis = 9

# the hypothesis talks about the number of kg of grapes and mangoes purchased by Andrew, referenced also in the premise
if grapes_kg_hypothesis <= grapes_kg_premise:
    # check if the hypothesis value contradicts the estimate of more than 'grapes_kg_premise'
    label = "contradiction"
elif mangoes_kg_hypothesis!= mangoes_kg_premise:
    # check if the number of kg of mangoes in the hypothesis contradicts the number of kg of mangoes reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of kg of grapes
    # any number of kg of grapes greater than 'grapes_kg_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
