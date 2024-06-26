share_premise = 600
share_hypothesis = 500

# the hypothesis refers to Greg's share mentioned in the premise
if share_premise <= share_hypothesis:
    # check if the estimate of'share_hypothesis' contradicts the share value in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
