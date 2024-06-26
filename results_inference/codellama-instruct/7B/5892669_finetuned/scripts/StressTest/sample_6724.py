amount_premise = 1600
amount_hypothesis = 3600

# the hypothesis refers to the amount from Anwar mentioned in the premise
if amount_hypothesis <= amount_premise:
    # check if the amount in the hypothesis contradicts the estimate of more than 'amount_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the amount
    # any amount greater than 'amount_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)