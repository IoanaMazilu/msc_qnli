grapes_purchased_premise = 1
grapes_purchased_hypothesis = 7
rate_grapes_premise = 68
rate_grapes_hypothesis = 68
rate_mangoes_premise = 48
rate_mangoes_hypothesis = 48

# the hypothesis refers to the amount of grapes and mangoes purchased by Andrew, as mentioned in the premise
if grapes_purchased_hypothesis!= grapes_purchased_premise:
    # check if the amount of grapes purchased in the hypothesis contradicts the amount of grapes purchased in the premise
    label = "contradiction"
elif rate_grapes_hypothesis!= rate_grapes_premise or rate_mangoes_hypothesis!= rate_mangoes_premise:
    # check if the rate of grapes or mangoes in the hypothesis contradicts the rate of grapes or mangoes in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
