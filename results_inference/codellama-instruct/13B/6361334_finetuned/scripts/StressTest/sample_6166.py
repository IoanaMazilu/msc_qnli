gift_premise = 85
gift_hypothesis = 95

# the hypothesis refers to the amount of money to be given to John, which is also mentioned in the premise
if gift_hypothesis <= gift_premise:
    # check if the hypothesis value contradicts the estimate of more than 'gift_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the amount of money to be given to John
    # any amount of money greater than 'gift_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
