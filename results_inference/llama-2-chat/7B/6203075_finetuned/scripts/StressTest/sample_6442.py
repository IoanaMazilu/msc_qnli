grapes_premise = 1
grapes_hypothesis = 7
rate_grapes_premise = 68
rate_grapes_hypothesis = 68
mangoes_premise = 9
mangoes_hypothesis = 9
rate_mangoes_premise = 48
rate_mangoes_hypothesis = 48

# the hypothesis refers to the amount of grapes and mangoes purchased by Andrew
if grapes_hypothesis <= grapes_premise:
    # check if the amount of grapes in the hypothesis contradicts the amount of grapes in the premise
    label = "contradiction"
elif rate_grapes_hypothesis!= rate_grapes_premise:
    # check if the rate of grapes in the hypothesis contradicts the rate of grapes in the premise
    label = "contradiction"
elif mangoes_hypothesis!= mangoes_premise:
    # check if the amount of mangoes in the hypothesis contradicts the amount of mangoes in the premise
    label = "contradiction"
elif rate_mangoes_hypothesis!= rate_mangoes_premise:
    # check if the rate of mangoes in the hypothesis contradicts the rate of mangoes in the premise
    label = "contradiction"
else:
    # if the hypothesis values and rates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
