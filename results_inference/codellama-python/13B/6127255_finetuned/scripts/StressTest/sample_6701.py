tony_share_premise = 4500
tony_share_hypothesis = 7500

# the hypothesis refers to the share of Tony mentioned in the premise
if tony_share_hypothesis!= tony_share_premise:
    # check if the share of Tony in the hypothesis contradicts the share of Tony reported in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
