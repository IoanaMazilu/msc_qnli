share_premise = 4500
share_hypothesis = 6500

# the hypothesis refers to the share mentioned in the premise
if share_hypothesis >= share_premise:
    # check if the estimate of'share_hypothesis' contradicts the share mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise value, we can infer entailment
    label = "entailment"

print(label)
