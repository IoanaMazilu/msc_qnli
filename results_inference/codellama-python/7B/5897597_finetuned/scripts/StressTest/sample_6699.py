share_tony_premise = 4500
share_tony_hypothesis = 6500

# the hypothesis refers to Tony's share mentioned in the premise
if share_tony_premise >= share_tony_hypothesis:
    # check if the share in the premise contradicts the estimate of less than'share_tony_hypothesis'
    label = "contradiction"
else:
    # if the share in the premise does not contradict the hypothesis, we can infer entailment
    label = "entailment"

print(label)
