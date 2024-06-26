withdrawal_premise = 14000
withdrawal_hypothesis = 44000

# the hypothesis refers to the amount withdrawn by John, mentioned in the premise
if withdrawal_premise <= withdrawal_hypothesis:
    # check if the estimate of 'withdrawal_hypothesis' contradicts the amount withdrawn in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the amount withdrawn
    # any amount greater than 'withdrawal_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
