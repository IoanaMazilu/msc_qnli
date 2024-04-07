# Premise: Andrew purchased 8 kg of grapes at the rate of 70 per kg and 9 kg of mangoes at the rate of 55 per kg.
# Hypothesis: Andrew purchased more than 8 kg of grapes at the rate of 70 per kg and 9 kg of mangoes at the rate of 55 per kg.
# Golden Label: contradiction

grapes_kg_premise = 8
grapes_kg_hypothesis = 8
grapes_rate_premise = 70
grapes_rate_hypothesis = 70
mangoes_kg_premise = 9
mangoes_kg_hypothesis = 9
mangoes_rate_premise = 55
mangoes_rate_hypothesis = 55

# the hypothesis talks about the amount of grapes and mangoes purchased, as well as their rates, all mentioned in the premise
if grapes_kg_hypothesis <= grapes_kg_premise:
    # check if the hypothesis value contradicts the premise of 'grapes_kg_premise'
    label = "contradiction"
elif grapes_rate_hypothesis != grapes_rate_premise or mangoes_rate_hypothesis != mangoes_rate_premise:
    # check if the rates in the hypothesis contradict the rates mentioned in the premise
    label = "contradiction"
elif mangoes_kg_hypothesis != mangoes_kg_premise:
    # check if the amount of mangoes in the hypothesis contradicts the amount in the premise
    label = "contradiction"
else:
    # the premise gives exact values for the amount of fruits purchased and their rates
    # any value that is not explicitly mentioned in the premise, even if it does not contradict the premise, cannot be entailed from the premise
    label = "neutral"

print(label)

