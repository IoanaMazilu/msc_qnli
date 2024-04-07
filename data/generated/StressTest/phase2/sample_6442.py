# Premise: Andrew purchased more than 1 kg of grapes at the rate of 68 per kg and 9 kg of mangoes at the rate of 48 per kg.
# Hypothesis: Andrew purchased 7 kg of grapes at the rate of 68 per kg and 9 kg of mangoes at the rate of 48 per kg.
# Golden Label: neutral

grapes_kg_premise = 1
grapes_kg_hypothesis = 7
rate_grapes_premise = 68
rate_grapes_hypothesis = 68
mangoes_kg_premise = 9
mangoes_kg_hypothesis = 9
rate_mangoes_premise = 48
rate_mangoes_hypothesis = 48

# the hypothesis refers to the quantities and rates of purchased grapes and mangoes mentioned in the premise
if grapes_kg_hypothesis <= grapes_kg_premise:
    # check if the quantity of grapes in the hypothesis contradicts the estimate of more than 'grapes_kg_premise' in the premise
    label = "contradiction"
elif rate_grapes_hypothesis != rate_grapes_premise or rate_mangoes_hypothesis != rate_mangoes_premise:
    # check if the rates in the hypothesis contradict the rates in the premise
    label = "contradiction"
elif mangoes_kg_hypothesis != mangoes_kg_premise:
    # check if the quantity of mangoes in the hypothesis contradicts the quantity in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the quantity of grapes
    # any quantity of grapes greater than 'grapes_kg_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

