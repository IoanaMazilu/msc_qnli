# Premise: Andrew purchased more than 5 kg of grapes at the rate of 70 per kg and 9 kg of mangoes at the rate of 55 per kg.
# Hypothesis: Andrew purchased 8 kg of grapes at the rate of 70 per kg and 9 kg of mangoes at the rate of 55 per kg.
# Golden Label: neutral

grapes_weight_premise = 5
grapes_weight_hypothesis = 8
grapes_rate_premise = 70
grapes_rate_hypothesis = 70
mangoes_weight_premise = 9
mangoes_weight_hypothesis = 9
mangoes_rate_premise = 55
mangoes_rate_hypothesis = 55

# the hypothesis talks about the quantity and rate of grapes and mangoes purchased, which is also mentioned in the premise
if grapes_weight_hypothesis <= grapes_weight_premise:
    # check if the weight of grapes purchased in the hypothesis contradicts the premise of purchasing more than 'grapes_weight_premise' kg of grapes
    label = "contradiction"
elif grapes_rate_hypothesis != grapes_rate_premise:
    # check if the rate of purchasing grapes in the hypothesis contradicts the rate mentioned in the premise
    label = "contradiction"
elif mangoes_weight_hypothesis != mangoes_weight_premise:
    # check if the weight of mangoes purchased in the hypothesis contradicts the weight mentioned in the premise
    label = "contradiction"
elif mangoes_rate_hypothesis != mangoes_rate_premise:
    # check if the rate of purchasing mangoes in the hypothesis contradicts the rate mentioned in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for grapes' weight, any value greater than 'grapes_weight_premise' does not contradict the premise but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

