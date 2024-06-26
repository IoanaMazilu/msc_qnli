deepak_share_premise = 1300
deepak_share_hypothesis = 4300

# the hypothesis refers to the share of Deepak mentioned in the premise
if deepak_share_premise >= deepak_share_hypothesis:
    # check if the estimate of 'deepak_share_premise' contradicts the hypothesis
    label = "contradiction"
elif deepak_share_premise < deepak_share_hypothesis:
    # if the share of Deepak in the premise is less than the one in the hypothesis, we can infer entailment
    label = "entailment"
else:
    # if the share of Deepak in the premise is equal to the one in the hypothesis, we can infer neutrality
    label = "neutral"

print(label)
