gift_premise = 95
gift_hypothesis = 55

# the hypothesis refers to the amount of money mentioned in the premise
if gift_hypothesis <= gift_premise:
    # check if the estimate of 'gift_hypothesis' contradicts the amount of money in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the amount of money
    # any amount of money greater than 'gift_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
