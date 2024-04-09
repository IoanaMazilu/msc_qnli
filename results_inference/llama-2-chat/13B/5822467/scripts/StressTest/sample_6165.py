gift_amount_premise = 95
gift_amount_hypothesis = 85

# the hypothesis refers to the amount of money to be given to John
if gift_amount_hypothesis <= gift_amount_premise:
    # check if the hypothesis value contradicts the estimate of 'gift_amount_premise'
    label = "contradiction"
elif gift_amount_premise!= gift_amount_hypothesis:
    # check if the hypothesis value contradicts the amount of money to be given in the premise
    label = "contradiction"
else:
    # if the hypothesis value and the premise value do not contradict, we can infer neutrality
    label = "neutral"

print(label)
