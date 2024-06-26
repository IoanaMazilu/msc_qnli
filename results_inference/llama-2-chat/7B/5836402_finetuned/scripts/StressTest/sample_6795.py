deposit_premise = 62500
deposit_hypothesis = 22500

# the hypothesis refers to the deposit amount mentioned in the premise
if deposit_premise <= deposit_hypothesis:
    # check if the estimate of 'deposit_hypothesis' contradicts the deposit amount in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
