deepak_share_premise = 1300
deepak_share_hypothesis = 1300

# the hypothesis refers to Deepak's share mentioned in the premise
if deepak_share_hypothesis >= deepak_share_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
