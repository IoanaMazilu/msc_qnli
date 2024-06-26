grapes_kg_premise = 11
grapes_rate_premise = 98
mangoes_kg_premise = 7
mangoes_rate_premise = 50

grapes_kg_hypothesis = 21
grapes_rate_hypothesis = 98
mangoes_kg_hypothesis = 7
mangoes_rate_hypothesis = 50

# the hypothesis refers to the quantity and rate of grapes and mangoes purchased by Andrew mentioned in the premise
if grapes_kg_premise != grapes_kg_hypothesis or grapes_rate_premise != grapes_rate_hypothesis:
    # check if the number of kg of grapes or the rate per kg in the hypothesis contradicts the premise
    label = "contradiction"
elif mangoes_kg_premise != mangoes_kg_hypothesis or mangoes_rate_premise != mangoes_rate_hypothesis:
    # check if the number of kg of mangoes or the rate per kg in the hypothesis contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
