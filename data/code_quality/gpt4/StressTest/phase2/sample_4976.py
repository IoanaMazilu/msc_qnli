share_difference_premise = 300
share_difference_hypothesis = 800

# the hypothesis refers to the difference between Raja and Rahim's share, also mentioned in the premise
if share_difference_premise != share_difference_hypothesis:
    # check if the 'share_difference_hypothesis' contradicts the difference mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
