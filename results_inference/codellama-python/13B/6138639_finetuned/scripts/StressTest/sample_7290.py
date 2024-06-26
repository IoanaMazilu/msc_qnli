share_premise = 600
share_hypothesis = 500

# the hypothesis refers to the share of Greg mentioned in the premise
if share_premise <= share_hypothesis:
    # check if the estimate of'share_hypothesis' contradicts the share of Greg in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
