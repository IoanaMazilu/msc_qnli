# Premise: Andrew purchased 11 kg of grapes at the rate of 98 per kg and 7 kg of mangoes at the rate of 50 per kg.
# Hypothesis: Andrew purchased less than 51 kg of grapes at the rate of 98 per kg and 7 kg of mangoes at the rate of 50 per kg.
# Golden Label: entailment

grapes_purchased_premise = 11
grapes_purchased_hypothesis = 51
mangoes_purchased_premise = 7
mangoes_purchased_hypothesis = 7
grape_rate_premise = 98
grape_rate_hypothesis = 98
mango_rate_premise = 50
mango_rate_hypothesis = 50

# the hypothesis refers to the weight of the purchased grapes and mangoes, as well as their rates which are mentioned in the premise 
if grapes_purchased_hypothesis >= grapes_purchased_premise:
    # check if the estimate of 'grapes_purchased_hypothesis' contradicts the weight of purchased grapes in the premise
    label = "contradiction"
elif mangoes_purchased_hypothesis != mangoes_purchased_premise:
    # check if the weight of purchased mangoes in the hypothesis contradicts the weight of purchased mangoes in the premise
    label = "contradiction"
elif grape_rate_hypothesis != grape_rate_premise:
    # check if the rate of grapes in the hypothesis contradicts the rate of grapes in the premise
    label = "contradiction"
elif mango_rate_hypothesis != mango_rate_premise:
    # check if the rate of mangoes in the hypothesis contradicts the rate of mangoes in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

