grapes_kg_premise = 7
grapes_kg_hypothesis = 1
grapes_rate_premise = 68
grapes_rate_hypothesis = 68
mangoes_kg_premise = 9
mangoes_kg_hypothesis = 9
mangoes_rate_premise = 48
mangoes_rate_hypothesis = 48

# the hypothesis refers to the purchased amounts of grapes and mangoes mentioned in the premise
if grapes_kg_hypothesis <= grapes_kg_premise:
    # check if the hypothesis value contradicts the premise value of 'grapes_kg_premise'
    label = "contradiction"
elif mangoes_kg_hypothesis!= mangoes_kg_premise:
    # check if the hypothesis value contradicts the premise value of'mangoes_kg_premise'
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
