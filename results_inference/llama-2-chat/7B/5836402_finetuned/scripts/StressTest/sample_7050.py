share_premise = 1300
share_hypothesis = 4300

# the hypothesis refers to the share of Deepak mentioned in the premise
if share_hypothesis >= share_premise:
    # check if the estimate of'share_hypothesis' contradicts the share mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise value, we can infer entailment
    label = "entailment"

print(label)
