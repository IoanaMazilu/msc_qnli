deepak_share_premise = 4300
deepak_share_hypothesis = 1300

# the hypothesis refers to the share of Deepak, mentioned in the premise
if deepak_share_premise <= deepak_share_hypothesis:
    # check if the estimate of 'deepak_share_hypothesis' contradicts the share of Deepak reported in the premise
    label = "contradiction"
elif deepak_share_hypothesis!= deepak_share_premise:
    # check if the share of Deepak in the hypothesis contradicts the share reported in the premise
    label = "contradiction"
else:
    # if the hypothesis value and estimate do not contradict the premise, we can infer entailment
    label = "entailment"

print(label)
