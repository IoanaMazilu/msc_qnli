deposit_premise = 22500
deposit_hypothesis = 62500

# the hypothesis talks about the amount of money Lucy deposited, referenced also in the premise
if deposit_hypothesis <= deposit_premise:
    # check if the hypothesis value contradicts the estimate of more than 'deposit_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the amount of money deposited
    # any amount greater than 'deposit_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
# 