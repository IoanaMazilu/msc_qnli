deepak_share_premise = 1300
deepak_share_hypothesis = 4300

# the hypothesis refers to the share of Deepak mentioned in the premise
if deepak_share_premise >= deepak_share_hypothesis:
    # check if the estimate of 'deepak_share_hypothesis' contradicts the share of Deepak in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
