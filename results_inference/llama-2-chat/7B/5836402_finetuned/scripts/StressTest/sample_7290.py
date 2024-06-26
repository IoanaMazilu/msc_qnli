share_premise = 600
share_hypothesis = 500

# the hypothesis refers to the amount of Greg's share mentioned in the premise
if share_hypothesis >= share_premise:
    # check if the hypothesis value contradicts the amount of Greg's share in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise value, we can infer entailment
    label = "entailment"

print(label)
