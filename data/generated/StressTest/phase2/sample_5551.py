# Premise: Andrew purchased less than 7 kg of grapes at the rate of 74 per kg and 9 kg of mangoes at the rate of 59 per kg.
# Hypothesis: Andrew purchased 6 kg of grapes at the rate of 74 per kg and 9 kg of mangoes at the rate of 59 per kg.
# Golden Label: neutral

grapes_kg_premise = 7
grapes_kg_hypothesis = 6
grapes_rate_premise = 74
grapes_rate_hypothesis = 74
mangoes_kg_premise = 9
mangoes_kg_hypothesis = 9
mangoes_rate_premise = 59
mangoes_rate_hypothesis = 59

# the hypothesis refers to the quantities and rates of grapes and mangoes purchased by Andrew, mentioned in the premise
if grapes_kg_hypothesis >= grapes_kg_premise:
    # check if the quantity of grapes in the hypothesis contradicts the premise's estimate of less than 'grapes_kg_premise' kg
    label = "contradiction"
elif grapes_rate_hypothesis != grapes_rate_premise or mangoes_rate_hypothesis != mangoes_rate_premise:
    # check if the rates in the hypothesis contradict the rates mentioned in the premise
    label = "contradiction"
elif mangoes_kg_hypothesis != mangoes_kg_premise:
    # check if the quantity of mangoes in the hypothesis contradicts the quantity mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

