tony_share_premise = 4500
tony_share_hypothesis = 6500

# the hypothesis refers to the share of Tony mentioned in the premise
if tony_share_hypothesis <= tony_share_premise:
    # check if the estimate of 'tony_share_hypothesis' contradicts the share of Tony in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
