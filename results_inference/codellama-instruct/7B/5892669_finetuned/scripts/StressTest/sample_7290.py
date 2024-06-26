share_value_premise = 600
share_value_hypothesis = 500

# the hypothesis refers to the value of Greg's share mentioned in the premise
if share_value_premise <= share_value_hypothesis:
    # check if the estimate of'share_value_hypothesis' contradicts the value of Greg's share in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
