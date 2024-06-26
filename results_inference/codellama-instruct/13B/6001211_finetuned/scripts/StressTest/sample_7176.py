total_amount_premise = 4800
total_amount_hypothesis = 3800

# the hypothesis refers to the total amount mentioned in the premise
if total_amount_premise <= total_amount_hypothesis:
    # check if the estimate of 'total_amount_hypothesis' contradicts the total amount in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
