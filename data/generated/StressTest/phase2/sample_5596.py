# Premise: Andrew purchased less than 70 kg of grapes at the rate of 82 per kg and 6 kg of mangoes at the rate of 62 per kg.
# Hypothesis: Andrew purchased 10 kg of grapes at the rate of 82 per kg and 6 kg of mangoes at the rate of 62 per kg.
# Golden Label: neutral

grapes_weight_premise = 70
grapes_weight_hypothesis = 10
grapes_rate_premise = 82
grapes_rate_hypothesis = 82
mangoes_weight_premise = 6
mangoes_weight_hypothesis = 6
mangoes_rate_premise = 62
mangoes_rate_hypothesis = 62

# the hypothesis refers to the quantities and rates of purchasing grapes and mangoes mentioned in the premise
if grapes_weight_hypothesis >= grapes_weight_premise:
    # check if the weight of grapes purchased in the hypothesis contradicts the premise's estimate of less than 'grapes_weight_premise'
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
    # the hypothesis values and estimates do not contradict the premise ones, but the premise gives only an estimate for the weight of grapes
    # any weight of grapes less than 'grapes_weight_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

