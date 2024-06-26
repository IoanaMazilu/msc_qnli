deepak_share_premise = 1300
deepak_share_hypothesis = 4300

# the hypothesis refers to Deepak's share mentioned in the premise
if deepak_share_premise >= deepak_share_hypothesis:
    # check if the premise contradicts the hypothesis
    label = "contradiction"
else:
    # if the premise value is less than the hypothesis value, it is consistent
    # but we cannot infer entailment because the hypothesis value is not explicitly mentioned in the premise
    label = "neutral"

print(label)
