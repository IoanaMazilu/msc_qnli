# Premise: Andrew purchased 8 kg of grapes at the rate of 70 per kg and 9 kg of mangoes at the rate of 55 per kg.
# Hypothesis: Andrew purchased more than 5 kg of grapes at the rate of 70 per kg and 9 kg of mangoes at the rate of 55 per kg.
# Golden Label: entailment

grapes_kg_premise = 8
grapes_kg_hypothesis = 5
grape_rate = 70
mangoes_kg_premise = 9
mangoes_kg_hypothesis = 9
mango_rate = 55

# the hypothesis refers to the quantities of grapes and mangoes bought by Andrew mentioned in the premise
if grapes_kg_hypothesis >= grapes_kg_premise:
    # check if the estimate of 'grapes_kg_hypothesis' contradicts the quantity of grapes in the premise
    label = "contradiction"
elif mangoes_kg_hypothesis != mangoes_kg_premise:
    # check if the quantity of mangoes in the hypothesis contradicts the quantity of mangoes mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

