# Premise: Harkamal purchased 8 kg of grapes at the rate of 70 per kg and 9 kg of mangoes at the rate of 55 per kg.
# Hypothesis: Harkamal purchased more than 2 kg of grapes at the rate of 70 per kg and 9 kg of mangoes at the rate of 55 per kg.
# Golden Label: entailment

grapes_kg_premise = 8
grapes_kg_hypothesis = 2
grapes_rate_premise = 70
grapes_rate_hypothesis = 70
mangoes_kg_premise = 9
mangoes_kg_hypothesis = 9
mangoes_rate_premise = 55
mangoes_rate_hypothesis = 55

# the hypothesis talks about the quantity and rate of purchased grapes and mangoes mentioned in the premise
if grapes_kg_premise < grapes_kg_hypothesis:
    # check if the hypothesis contradicts the quantity of purchased grapes in the premise
    label = "contradiction"
elif grapes_rate_premise != grapes_rate_hypothesis:
    # check if the rate of purchased grapes in the hypothesis contradicts the rate in the premise
    label = "contradiction"
elif mangoes_kg_premise != mangoes_kg_hypothesis:
    # check if the quantity of purchased mangoes in the hypothesis contradicts the quantity in the premise
    label = "contradiction"
elif mangoes_rate_premise != mangoes_rate_hypothesis:
    # check if the rate of purchased mangoes in the hypothesis contradicts the rate in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

