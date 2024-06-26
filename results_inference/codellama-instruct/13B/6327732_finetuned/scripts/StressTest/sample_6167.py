amount_premise = 95
amount_hypothesis = 95

# the hypothesis refers to the amount of money mentioned in the premise
if amount_hypothesis >= amount_premise:
    # check if the estimate of 'amount_hypothesis' contradicts the amount of money in the premise
    label = "contradiction"
else:
    # the premise gives an exact amount of money to give
    # any amount less than 'amount_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
