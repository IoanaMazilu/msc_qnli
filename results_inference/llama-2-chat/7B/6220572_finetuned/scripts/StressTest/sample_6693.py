withdrawals_premise = 14000
withdrawals_hypothesis = 44000

# the hypothesis talks about the number of withdrawals, referenced also in the premise
if withdrawals_hypothesis <= withdrawals_premise:
    # check if the hypothesis value contradicts the number of withdrawals in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of withdrawals
    # any number of withdrawals greater than 'withdrawals_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
