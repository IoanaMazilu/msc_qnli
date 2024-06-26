amount_premise = 95
amount_hypothesis = 55

# the hypothesis refers to the amount of money to be given to John
if amount_hypothesis <= amount_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
else:
    # the premise gives an exact amount, while the hypothesis gives a lower amount
    # any lower amount is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
