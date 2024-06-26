deepak_share_premise = 4300
deepak_share_hypothesis = 1300

# the hypothesis refers to the Deepak's share that is also mentioned in the premise
if deepak_share_hypothesis >= deepak_share_premise:
    # check if the value in the hypothesis contradicts the estimate of less than 'deepak_share_premise'
    label = "contradiction"
elif deepak_share_hypothesis < deepak_share_premise:
    # if the hypothesis value is less than the premise one, we can infer entailment
    label = "entailment"
else:
    # if the hypothesis value does not contradict the premise one, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
