sameer_share_premise = 6970
sameer_share_hypothesis = 1970

# the hypothesis refers to the share of Sameer mentioned in the premise
if sameer_share_premise <= sameer_share_hypothesis:
    # check if the estimate of'sameer_share_hypothesis' contradicts the share of Sameer in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
