withdrawal_premise = 14000
withdrawal_hypothesis = 44000

# the hypothesis refers to the amount withdrawn by John after 8 months
if withdrawal_hypothesis >= withdrawal_premise:
    # check if the hypothesis value contradicts the amount withdrawn in the premise
    label = "contradiction"
else:
    # the premise gives an estimate for the amount withdrawn by John
    # any amount less than 'withdrawal_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
