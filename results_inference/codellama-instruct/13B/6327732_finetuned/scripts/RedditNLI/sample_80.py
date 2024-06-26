amount_premise = 5.1
amount_hypothesis = 5.1

# the hypothesis and premise mention the same amount of money for the deal
if amount_premise!= amount_hypothesis:
    # check if the amount in the hypothesis contradicts the amount in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the amount of money
    # any estimate of the amount in the hypothesis greater or equal to 'amount_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
