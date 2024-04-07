# Premise: Andrew purchased 14 kg of grapes at the rate of 54 per kg and 10 kg of mangoes at the rate of 62 per kg.
# Hypothesis: Andrew purchased less than 84 kg of grapes at the rate of 54 per kg and 10 kg of mangoes at the rate of 62 per kg.
# Golden Label: entailment

grapes_weight_premise = 14
grapes_weight_hypothesis = 84
grapes_rate_premise = 54
grapes_rate_hypothesis = 54
mangoes_weight_premise = 10
mangoes_weight_hypothesis = 10
mangoes_rate_premise = 62
mangoes_rate_hypothesis = 62

# the hypothesis refers to the weight and rate of grapes and mangoes purchased by Andrew mentioned in the premise
if grapes_weight_premise >= grapes_weight_hypothesis:
    # check if the estimate of 'grapes_weight_hypothesis' contradicts the weight of grape purchases in the premise
    label = "contradiction"
elif grapes_rate_hypothesis != grapes_rate_premise or mangoes_rate_hypothesis != mangoes_rate_premise or mangoes_weight_hypothesis != mangoes_weight_premise:
    # check if the rate of grape purchases, the weight or rate of mango purchases in the hypothesis contradicts the rates and weight reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

