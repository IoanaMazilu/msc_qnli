deposit_premise = 22500
deposit_hypothesis = 62500

# the hypothesis refers to the amount of money deposited by Lucy, which is also mentioned in the premise
if deposit_hypothesis <= deposit_premise:
    # check if the amount of money deposited in the hypothesis contradicts the estimate of more than 'deposit_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the amount of money deposited
    # any amount greater than 'deposit_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)