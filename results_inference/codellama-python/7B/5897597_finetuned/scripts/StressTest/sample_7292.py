greg_share_premise = 600
greg_share_hypothesis = 400

# the hypothesis refers to Greg's share mentioned in the premise
if greg_share_hypothesis!= greg_share_premise:
    # check if the value of Greg's share in the hypothesis contradicts the value of Greg's share reported in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
