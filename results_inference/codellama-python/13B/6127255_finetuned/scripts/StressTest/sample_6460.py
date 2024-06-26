deposit_premise = 72500
deposit_hypothesis = 62500

# the hypothesis talks about the amount of money Lucy deposited, which is also mentioned in the premise
if deposit_hypothesis >= deposit_premise:
    # check if the deposit amount in the hypothesis contradicts the estimate of less than 'deposit_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the deposit amount
    # any deposit amount less than 'deposit_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
