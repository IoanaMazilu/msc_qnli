withdrawal_amount_premise = 14000
withdrawal_amount_hypothesis = 44000

# the hypothesis gives an estimate for the withdrawal amount
if withdrawal_amount_hypothesis <= withdrawal_amount_premise:
    # check if the hypothesis value contradicts the withdrawal amount in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the withdrawal amount
    # any number greater than 'withdrawal_amount_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
