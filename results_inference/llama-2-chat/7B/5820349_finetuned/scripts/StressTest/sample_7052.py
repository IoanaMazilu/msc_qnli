deepak_share_premise = 1300
deepak_share_hypothesis = 1300

# the hypothesis refers to Deepak's share mentioned in the premise
if deepak_share_hypothesis >= deepak_share_premise:
    # check if the estimate of 'deepak_share_hypothesis' contradicts the number of Deepak's share in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
