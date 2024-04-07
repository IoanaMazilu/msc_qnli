# Premise: Bruce purchased more than 3 kg of grapes at the rate of 70 per kg and 9 kg of mangoes at the rate of 55 per kg.
# Hypothesis: Bruce purchased 8 kg of grapes at the rate of 70 per kg and 9 kg of mangoes at the rate of 55 per kg.
# Golden Label: neutral

grapes_purchased_premise = 3
grapes_purchased_hypothesis = 8
rate_grapes_premise = 70
rate_grapes_hypothesis = 70
mangoes_purchased_premise = 9
mangoes_purchased_hypothesis = 9
rate_mangoes_premise = 55
rate_mangoes_hypothesis = 55

# the hypothesis refers to the number and rate of purchased grapes and mangoes mentioned in the premise
if grapes_purchased_hypothesis <= grapes_purchased_premise:
    # check if the hypothesis value contradicts the estimate of more than 'grapes_purchased_premise' 
    label = "contradiction"
elif rate_grapes_hypothesis != rate_grapes_premise:
    # check if the rate of grapes in the hypothesis contradicts the rate of grapes in the premise
    label = "contradiction"
elif mangoes_purchased_hypothesis != mangoes_purchased_premise:
    # check if the number of purchased mangoes in the hypothesis contradicts the number of purchased mangoes in the premise
    label = "contradiction"
elif rate_mangoes_hypothesis != rate_mangoes_premise:
    # check if the rate of mangoes in the hypothesis contradicts the rate of mangoes in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of purchased grapes
    # any number of grapes greater than 'grapes_purchased_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

