gift_amount_premise = 85
gift_amount_hypothesis = 95

# the hypothesis refers to the amount of money to be given to John
if gift_amount_hypothesis <= gift_amount_premise:
    # check if the hypothesis value contradicts the estimate of more than 'gift_amount_premise'
    label = "contradiction"
elif gift_amount_premise!= gift_amount_hypothesis:
    # check if the hypothesis value contradicts the amount of money reported in the premise
    label = "contradiction"
else:
    # if the hypothesis value and estimate do not contradict the premise, we can infer entailment
    label = "entailment"

print(label)
