deposit_premise = 22500
deposit_hypothesis = 62500

# the hypothesis refers to the amount of money Lucy deposited, which is also mentioned in the premise
if deposit_hypothesis <= deposit_premise:
    # check if the hypothesis value contradicts the premise's estimate of more than 'deposit_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the deposit amount
    # any deposit amount greater than 'deposit_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
