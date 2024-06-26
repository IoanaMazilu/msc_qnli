deposit_premise = 62500
deposit_hypothesis = 22500

# the hypothesis refers to the amount deposited in the investment fund mentioned in the premise
if deposit_hypothesis <= deposit_premise:
    # check if the estimate of 'deposit_hypothesis' contradicts the amount deposited in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the amount deposited
    # any amount greater than 'deposit_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
