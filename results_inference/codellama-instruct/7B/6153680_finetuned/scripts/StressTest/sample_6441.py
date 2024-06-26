grapes_purchased_premise = 7
grapes_purchased_hypothesis = 1
grapes_rate_premise = 68
grapes_rate_hypothesis = 68
mangoes_purchased_premise = 9
mangoes_purchased_hypothesis = 9
mangoes_rate_premise = 48
mangoes_rate_hypothesis = 48

# the hypothesis refers to the purchase of grapes and mangoes mentioned in the premise
if grapes_purchased_hypothesis <= grapes_purchased_premise and mangoes_purchased_hypothesis == mangoes_purchased_premise and grapes_rate_hypothesis == grapes_rate_premise and mangoes_rate_hypothesis == mangoes_rate_premise:
    # check if the hypothesis values contradict the premise values
    label = "contradiction"
elif grapes_purchased_hypothesis > grapes_purchased_premise or mangoes_purchased_hypothesis!= mangoes_purchased_premise or grapes_rate_hypothesis!= grapes_rate_premise or mangoes_rate_hypothesis!= mangoes_rate_premise:
    # check if the hypothesis values contradict the premise values
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
