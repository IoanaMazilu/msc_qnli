deposit_premise = 22500
deposit_hypothesis = 62500

# the hypothesis talks about the deposit amount, which is also mentioned in the premise
if deposit_hypothesis <= deposit_premise:
    # check if the hypothesis value contradicts the estimate of more than 'deposit_premise'
    label = "contradiction"
else:
    # the hypothesis value is greater than the premise value, so it does not contradict the premise
    label = "entailment"

print(label)
