lucy_deposit_premise = 72500
lucy_deposit_hypothesis = 62500

# the hypothesis refers to the amount of money Lucy deposited
if lucy_deposit_hypothesis <= lucy_deposit_premise:
    # check if the hypothesis value contradicts the estimate of 'lucy_deposit_premise'
    label = "contradiction"
elif lucy_deposit_hypothesis > lucy_deposit_premise:
    # check if the hypothesis value entails the premise value
    label = "entailment"
else:
    # the premise gives only an estimate for the amount of money Lucy deposited
    # any amount of money less than or equal to 'lucy_deposit_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
