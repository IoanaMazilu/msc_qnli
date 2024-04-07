# Premise: Harkamal purchased 8 kg of grapes at the rate of 70 per kg and 9 kg of mangoes at the rate of 55 per kg.
# Hypothesis: Harkamal purchased more than 4 kg of grapes at the rate of 70 per kg and 9 kg of mangoes at the rate of 55 per kg.
# Golden Label: entailment

grapes_purchased_premise = 8
grapes_purchased_hypothesis = 4
mangoes_purchased_premise = 9
mangoes_purchased_hypothesis = 9
rate_grapes = 70
rate_mangoes = 55

# the hypothesis refers to the quantity of grapes and mangoes purchased, mentioned in the premise
if grapes_purchased_hypothesis >= grapes_purchased_premise:
    # check if the hypothesis value contradicts the quantity of grapes purchased in the premise
    label = "contradiction"
elif mangoes_purchased_hypothesis != mangoes_purchased_premise:
    # check if the quantity of mangoes purchased in the hypothesis contradicts the quantity of mangoes purchased in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

