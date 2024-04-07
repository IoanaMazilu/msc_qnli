# Premise: Andrew purchased 7 kg of grapes at the rate of 68 per kg and 9 kg of mangoes at the rate of 48 per kg.
# Hypothesis: Andrew purchased less than 7 kg of grapes at the rate of 68 per kg and 9 kg of mangoes at the rate of 48 per kg.
# Golden Label: contradiction

grapes_weight_premise = 7
grapes_weight_hypothesis = 7
grapes_rate = 68
mangoes_weight_premise = 9
mangoes_weight_hypothesis = 9
mangoes_rate = 48

# the hypothesis talks about the weight of grapes and mangoes purchased by Andrew, mentioned in the premise
if grapes_weight_hypothesis >= grapes_weight_premise:
    # check if the hypothesis weight of grapes contradicts the premise
    label = "contradiction"
elif mangoes_weight_hypothesis != mangoes_weight_premise:
    # check if the weight of mangoes in the hypothesis contradicts the weight of mangoes in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

