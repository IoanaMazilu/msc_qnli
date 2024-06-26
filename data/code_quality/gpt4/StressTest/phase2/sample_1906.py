deposit_premise = 42500
deposit_hypothesis = 62500

# the hypothesis refers to the amount of money Lucy deposited, mentioned also in the premise
if deposit_hypothesis <= deposit_premise:
    # check if the amount of deposit in the hypothesis contradicts the estimate of more than 'deposit_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the amount of deposit
    # any amount greater than 'deposit_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
