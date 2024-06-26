amount_premise = 363
amount_hypothesis = 215

# the hypothesis and premise mention the amount of money needed by Fannie and Freddie
if amount_hypothesis < amount_premise:
    # check if the amount in the hypothesis contradicts the amount in the premise
    label = "contradiction"
else:
    # the premise gives an estimate for the amount of money needed
    # any estimate of the amount in the hypothesis greater or equal to the premise amount is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
