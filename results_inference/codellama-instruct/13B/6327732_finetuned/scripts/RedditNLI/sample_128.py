amount_premise = 7.2
amount_hypothesis = 7.15

# the hypothesis and premise mention the amount of money paid by Nestle to Starbucks
if amount_hypothesis < amount_premise:
    # check if the amount in the hypothesis contradicts the amount in the premise
    label = "contradiction"
else:
    # the premise gives an exact amount of money paid by Nestle to Starbucks
    # any amount in the hypothesis greater or equal to 'amount_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
