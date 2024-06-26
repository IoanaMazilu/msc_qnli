share_tony_premise = 4500
share_tony_hypothesis = 6500

# the hypothesis refers to the share of Tony mentioned in the premise
if share_tony_premise >= share_tony_hypothesis:
    # check if the value of'share_tony_premise' contradicts the estimate of less than'share_tony_hypothesis'
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
