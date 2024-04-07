# Premise: Andrew purchased less than 51 kg of grapes at the rate of 98 per kg and 7 kg of mangoes at the rate of 50 per kg.
# Hypothesis: Andrew purchased 11 kg of grapes at the rate of 98 per kg and 7 kg of mangoes at the rate of 50 per kg.
# Golden Label: neutral

grapes_kg_premise = 51
grapes_kg_hypothesis = 11
grapes_rate_premise = 98
grapes_rate_hypothesis = 98
mangoes_kg_premise = 7
mangoes_kg_hypothesis = 7
mangoes_rate_premise = 50
mangoes_rate_hypothesis = 50

# the hypothesis refers to the quantities of grapes and mangoes purchased mentioned in the premise
if grapes_kg_hypothesis >= grapes_kg_premise:
    # check if the hypothesis value contradicts the estimate of less than 'grapes_kg_premise'
    label = "contradiction"
elif grapes_rate_hypothesis != grapes_rate_premise:
    # check if the rate of grapes in the hypothesis contradicts the rate of grapes reported in the premise
    label = "contradiction"
elif mangoes_kg_hypothesis != mangoes_kg_premise:
    # check if the number of mangoes in the hypothesis contradicts the number of mangoes reported in the premise
    label = "contradiction"
elif mangoes_rate_hypothesis != mangoes_rate_premise:
    # check if the rate of mangoes in the hypothesis contradicts the rate of mangoes reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

