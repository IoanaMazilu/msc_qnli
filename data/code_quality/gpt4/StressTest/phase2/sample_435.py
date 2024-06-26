deepak_share_premise = 1380
deepak_share_hypothesis = 2380

# the hypothesis refers to the value of Deepak's share mentioned in the premise
if deepak_share_premise >= deepak_share_hypothesis:
    # check if the estimate of 'deepak_share_hypothesis' contradicts the value of Deepak's share in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
