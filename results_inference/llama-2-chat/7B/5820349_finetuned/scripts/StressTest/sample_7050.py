deepak_share_premise = 1300
deepak_share_hypothesis = 4300

# the hypothesis refers to Deepak's share mentioned in the premise
if deepak_share_premise >= deepak_share_hypothesis:
    # check if the value of 'deepak_share_premise' contradicts the estimate of less than 'deepak_share_hypothesis'
    label = "contradiction"
else:
    # if the premise value does not contradict the hypothesis estimate, we can infer entailment
    label = "entailment"

print(label)
