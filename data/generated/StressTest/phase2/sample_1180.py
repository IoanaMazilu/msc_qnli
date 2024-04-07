# Premise: Andrew purchased less than 84 kg of grapes at the rate of 54 per kg and 10 kg of mangoes at the rate of 62 per kg.
# Hypothesis: Andrew purchased 14 kg of grapes at the rate of 54 per kg and 10 kg of mangoes at the rate of 62 per kg.
# Golden Label: neutral

grapes_purchased_premise = 84
grapes_purchased_hypothesis = 14
grapes_rate_premise = 54
grapes_rate_hypothesis = 54
mangoes_purchased_premise = 10
mangoes_purchased_hypothesis = 10
mangoes_rate_premise = 62
mangoes_rate_hypothesis = 62

# the hypothesis refers to the quantities and rates of purchased grapes and mangoes mentioned in the premise
if grapes_purchased_hypothesis >= grapes_purchased_premise:
    # check if the quantity of 'grapes_purchased_hypothesis' contradicts the estimate of less than 'grapes_purchased_premise'
    label = "contradiction"
elif grapes_rate_hypothesis != grapes_rate_premise:
    # check if the rate of grapes in the hypothesis contradicts the rate mentioned in the premise
    label = "contradiction"
elif mangoes_purchased_hypothesis != mangoes_purchased_premise:
    # check if the quantity of mangoes in the hypothesis contradicts the quantity mentioned in the premise
    label = "contradiction"
elif mangoes_rate_hypothesis != mangoes_rate_premise:
    # check if the rate of mangoes in the hypothesis contradicts the rate mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

