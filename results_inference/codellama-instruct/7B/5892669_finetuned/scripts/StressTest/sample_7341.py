share_sameer_premise = 6970
share_sameer_hypothesis = 1970

# the hypothesis refers to the share of Sameer mentioned in the premise
if share_sameer_premise <= share_sameer_hypothesis:
    # check if the estimate of'share_sameer_hypothesis' contradicts the share of Sameer in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
