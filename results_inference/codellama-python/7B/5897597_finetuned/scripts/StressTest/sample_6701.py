share_premise = 4500
share_hypothesis = 7500

# the hypothesis refers to Tony's share mentioned in the premise
if share_hypothesis!= share_premise:
    # check if the share in the hypothesis contradicts the share reported in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
