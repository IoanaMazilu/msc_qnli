grapes_kg_premise = 1
grapes_rate_premise = 68
mangoes_kg_premise = 9
mangoes_rate_premise = 48

grapes_kg_hypothesis = 7
mangoes_kg_hypothesis = 9

# the hypothesis talks about the number of kg of grapes and mangoes purchased, referenced also in the premise
if grapes_kg_hypothesis <= grapes_kg_premise:
    # check if the hypothesis value contradicts the estimate of more than 'grapes_kg_premise'
    label = "contradiction"
elif mangoes_kg_hypothesis <= mangoes_kg_premise:
    # check if the hypothesis value contradicts the estimate of more than'mangoes_kg_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of kg of grapes and mangoes purchased
    # any number of kg greater than 'grapes_kg_premise' and'mangoes_kg_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
