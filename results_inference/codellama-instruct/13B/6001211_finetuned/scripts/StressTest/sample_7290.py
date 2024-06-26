share_premise = 600
share_hypothesis = 500

# the hypothesis refers to Greg's share mentioned in the premise
if share_premise <= share_hypothesis:
    # check if the estimate of'share_hypothesis' contradicts the share in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
