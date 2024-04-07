# Premise: Andrew purchased 7 kg of grapes at the rate of 68 per kg and 9 kg of mangoes at the rate of 48 per kg.
# Hypothesis: Andrew purchased more than 1 kg of grapes at the rate of 68 per kg and 9 kg of mangoes at the rate of 48 per kg.
# Golden Label: entailment

grapes_kg_premise = 7
grapes_kg_hypothesis = 1
grapes_rate_premise = 68
grapes_rate_hypothesis = 68
mangoes_kg_premise = 9
mangoes_kg_hypothesis = 9
mangoes_rate_premise = 48
mangoes_rate_hypothesis = 48

# the hypothesis refers to the quantity, rate of grapes and mangoes mentioned in the premise
if grapes_kg_premise <= grapes_kg_hypothesis:
    # check if the quantity of 'grapes_kg_hypothesis' contradicts the quantity of grapes in the premise
    label = "contradiction"
elif grapes_rate_premise != grapes_rate_hypothesis or mangoes_rate_premise != mangoes_rate_hypothesis:
    # check if the rate of grapes or mangoes in the hypothesis contradicts the rate of grapes or mangoes reported in the premise
    label = "contradiction"
elif mangoes_kg_hypothesis != mangoes_kg_premise:
    # check if the quantity of mangoes in the hypothesis contradicts the quantity of mangoes reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

