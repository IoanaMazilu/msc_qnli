deepak_share_premise = 1380
deepak_share_hypothesis = 3380

# The hypothesis states the share of Deepak which was also mentioned in the premise
if deepak_share_premise != deepak_share_hypothesis:
    # Check if Deepak's share in the hypothesis contradicts Deepak's share in the premise
    label = "contradiction"
else:
    # If Deepak's share in the hypothesis does not contradict Deepak's share in the premise, we can infer entailment
    label = "entailment"

print(label)
