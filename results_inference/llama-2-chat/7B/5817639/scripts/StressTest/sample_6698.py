withdrawals_premise = 2000
withdrawals_hypothesis = 7000

# the hypothesis talks about the amount of withdrawals, which is also referenced in the premise
if withdrawals_hypothesis <= withdrawals_premise:
    # check if the hypothesis value contradicts the estimate of 'withdrawals_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the amount of withdrawals
    # any amount of withdrawals greater than 'withdrawals_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
