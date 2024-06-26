grapes_weight_premise = 8
grapes_weight_hypothesis = 8
mangoes_weight_premise = 9
mangoes_weight_hypothesis = 9

# the hypothesis talks about the weight of grapes and mangoes purchased by Harkamal, which is also mentioned in the premise
if grapes_weight_hypothesis > grapes_weight_premise:
    # check if the hypothesis value contradicts the exact amount of 'grapes_weight_premise'
    label = "contradiction"
elif mangoes_weight_hypothesis != mangoes_weight_premise:
    # check if the weight of mangoes in the hypothesis contradicts the weight of mangoes mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
