total_share_premise = 4800
total_share_hypothesis = 3800

# the hypothesis refers to the total share among John, Jose & Binoy mentioned in the premise
if total_share_premise <= total_share_hypothesis:
    # check if the estimate of 'total_share_hypothesis' contradicts the total share in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
