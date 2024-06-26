lucy_deposit_premise = 62500
lucy_deposit_hypothesis = 22500

# the hypothesis talks about the amount of money Lucy deposited in the investment fund
# the premise gives an estimate for the amount of money Lucy deposited in the investment fund
if lucy_deposit_premise <= lucy_deposit_hypothesis:
    # check if the hypothesis value contradicts the estimate of 'lucy_deposit_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the amount of money Lucy deposited in the investment fund
    # any amount of money greater than 'lucy_deposit_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
