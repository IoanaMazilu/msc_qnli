deepak_share_premise = 1300
deepak_share_hypothesis = 1300

# the hypothesis talks about Deepak's share, which is also mentioned in the premise
if deepak_share_hypothesis >= deepak_share_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
else:
    # if the hypothesis value is less than the premise value, we can infer entailment
    label = "entailment"

print(label)