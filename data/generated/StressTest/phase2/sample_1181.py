# Premise: Andrew purchased 14 kg of grapes at the rate of 54 per kg and 10 kg of mangoes at the rate of 62 per kg.
# Hypothesis: Andrew purchased less than 14 kg of grapes at the rate of 54 per kg and 10 kg of mangoes at the rate of 62 per kg.
# Golden Label: contradiction

grapes_kg_premise = 14
grapes_rate_premise = 54
mangoes_kg_premise = 10
mangoes_rate_premise = 62

grapes_kg_hypothesis = 14
grapes_rate_hypothesis = 54
mangoes_kg_hypothesis = 10
mangoes_rate_hypothesis = 62

# the hypothesis refers to the number and rate of purchased grapes and mangoes mentioned in the premise
if grapes_kg_hypothesis >= grapes_kg_premise:
    # check if the hypothesis value contradicts the estimate of being less than 'grapes_kg_premise'
    label = "contradiction"
elif grapes_rate_hypothesis != grapes_rate_premise or mangoes_kg_hypothesis != mangoes_kg_premise or mangoes_rate_hypothesis != mangoes_rate_premise:
    # check if the rate of grapes or the number and rate of mangoes in the hypothesis contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

