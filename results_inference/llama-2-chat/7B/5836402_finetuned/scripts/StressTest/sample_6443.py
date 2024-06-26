grapes_weight_premise = 7
grapes_rate_premise = 68
mangoes_weight_premise = 9
mangoes_rate_premise = 48

grapes_weight_hypothesis = 7
grapes_rate_hypothesis = 68
mangoes_weight_hypothesis = 9
mangoes_rate_hypothesis = 48

# the hypothesis refers to the weight and rate of grapes and mangoes mentioned in the premise
if grapes_weight_hypothesis >= grapes_weight_premise:
    # check if the estimate of 'grapes_weight_hypothesis' contradicts the weight of grapes in the premise
    label = "contradiction"
elif grapes_rate_hypothesis!= grapes_rate_premise:
    # check if the rate of grapes in the hypothesis contradicts the rate of grapes reported in the premise
    label = "contradiction"
elif mangoes_weight_hypothesis!= mangoes_weight_premise:
    # check if the weight of mangoes in the hypothesis contradicts the weight of mangoes reported in the premise
    label = "contradiction"
elif mangoes_rate_hypothesis!= mangoes_rate_premise:
    # check if the rate of mangoes in the hypothesis contradicts the rate of mangoes reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
