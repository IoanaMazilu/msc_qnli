grapes_purchased_premise = 7
grapes_rate_premise = 68
mangoes_purchased_premise = 9
mangoes_rate_premise = 48

# the hypothesis refers to the number of grapes and mangoes purchased and their rates mentioned in the premise
if grapes_purchased_premise > grapes_rate_premise:
    # check if the estimate of 'grapes_purchased_premise' contradicts the number of grapes purchased in the premise
    label = "contradiction"
elif mangoes_purchased_premise > mangoes_rate_premise:
    # check if the estimate of'mangoes_purchased_premise' contradicts the number of mangoes purchased in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
