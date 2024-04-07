# Premise: Bruce purchased 8 kg of grapes at the rate of 70 per kg and 9 kg of mangoes at the rate of 55 per kg.
# Hypothesis: Bruce purchased 5 kg of grapes at the rate of 70 per kg and 9 kg of mangoes at the rate of 55 per kg.
# Golden Label: contradiction

grapes_kg_premise = 8
grapes_kg_hypothesis = 5
grapes_rate_premise = 70
grapes_rate_hypothesis = 70

mangoes_kg_premise = 9
mangoes_kg_hypothesis = 9
mangoes_rate_premise = 55
mangoes_rate_hypothesis = 55

# the hypothesis refers to the quantity and rate of grapes and mangoes purchased, mentioned in the premise

if grapes_kg_hypothesis > grapes_kg_premise:
    # check if the quantity of grapes purchased in the hypothesis contradicts the quantity of grapes purchased reported in the premise
    label = "contradiction"
elif grapes_rate_hypothesis != grapes_rate_premise:
    # check if the rate of grapes purchased in the hypothesis contradicts the rate of grapes purchased reported in the premise
    label = "contradiction"
elif mangoes_kg_hypothesis != mangoes_kg_premise:
    # check if the quantity of mangoes purchased in the hypothesis contradicts the quantity of mangoes purchased reported in the premise
    label = "contradiction"
elif mangoes_rate_hypothesis != mangoes_rate_premise:
    # check if the rate of mangoes purchased in the hypothesis contradicts the rate of mangoes purchased reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we infer entailment if the quantities and rates match, else it's neutral
    if grapes_kg_hypothesis == grapes_kg_premise and mangoes_kg_hypothesis == mangoes_kg_premise:
        label = "entailment"
    else:
        label = "neutral"

print(label)

