# Premise: Harkamal purchased 8 kg of grapes at the rate of 70 per kg and 9 kg of mangoes at the rate of 55 per kg.
# Hypothesis: Harkamal purchased 1 kg of grapes at the rate of 70 per kg and 9 kg of mangoes at the rate of 55 per kg.
# Golden Label: contradiction

grapes_weight_premise = 8
grapes_weight_hypothesis = 1
grapes_rate_premise = 70
grapes_rate_hypothesis = 70
mangoes_weight_premise = 9
mangoes_weight_hypothesis = 9
mangoes_rate_premise = 55
mangoes_rate_hypothesis = 55

# the hypothesis refers to the quantity and rate of grapes and mangoes purchased mentioned in the premise
if grapes_rate_premise != grapes_rate_hypothesis or mangoes_rate_premise != mangoes_rate_hypothesis:
    # check if the rate of grapes or mangoes contradicts the premise
    label = "contradiction"
elif grapes_weight_hypothesis > grapes_weight_premise or mangoes_weight_hypothesis > mangoes_weight_premise:
    # check if the quantity of grapes or mangoes in the hypothesis contradicts the premise
    label = "contradiction"
elif grapes_weight_hypothesis < grapes_weight_premise:
    # the premise clearly states the quantity of grapes, any lesser quantity cannot be explicitly entailed from the premise
    label = "neutral"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

