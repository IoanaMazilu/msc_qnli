#tony_withdraw_premise = 5000
#tony_withdraw_hypothesis = 2000

# the hypothesis talks about the amount Tony withdraws, which is also referenced in the premise
if tony_withdraw_hypothesis >= tony_withdraw_premise:
    # check if the hypothesis value contradicts the estimate of less than 'tony_withdraw_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the amount Tony withdraws
    # any amount less than 'tony_withdraw_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
#