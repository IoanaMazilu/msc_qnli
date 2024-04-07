# Premise: Andrew purchased 10 kg of grapes at the rate of 82 per kg and 6 kg of mangoes at the rate of 62 per kg.
# Hypothesis: Andrew purchased less than 70 kg of grapes at the rate of 82 per kg and 6 kg of mangoes at the rate of 62 per kg.
# Golden Label: entailment

grapes_kg_premise = 10
grapes_kg_hypothesis = 70
mangoes_kg_premise = 6
mangoes_kg_hypothesis = 6

# the hypothesis refers to the quantity of grapes and mangoes purchased by Andrew as mentioned in the premise
if grapes_kg_hypothesis < grapes_kg_premise:
    # check if the estimate of 'grapes_kg_hypothesis' contradicts the quantity of grapes purchased in the premise
    label = "contradiction"
elif mangoes_kg_hypothesis != mangoes_kg_premise:
    # check if the quantity of mangoes in the hypothesis contradicts the quantity of mangoes purchased as reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

