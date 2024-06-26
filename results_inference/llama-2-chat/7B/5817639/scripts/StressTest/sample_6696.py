withdrawal_premise = 2000
withdrawal_hypothesis = 5000

# the hypothesis talks about the amount of money withdrawn, referenced also in the premise
if withdrawal_hypothesis <= withdrawal_premise:
    # check if the hypothesis value contradicts the estimate of more than 'withdrawal_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the amount of money withdrawn
    # any amount of money withdrawn greater than 'withdrawal_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
