amount_premise = 7.2
amount_hypothesis = 7.15

# the premise and hypothesis mention a specific amount of money paid by Nestle to Starbucks
if amount_premise!= amount_hypothesis:
    # check if the amount in the hypothesis contradicts the amount in the premise
    label = "contradiction"
elif amount_hypothesis < amount_premise:
    # check if the estimated amount in the hypothesis contradicts the premise estimate
    label = "contradiction"
else:
    # the premise gives only an estimate for the amount
    # any estimate of the amount in the hypothesis greater or equal to the premise amount is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
