share_premise = 600
share_hypothesis = 400

# the hypothesis refers to the share amount mentioned in the premise
if share_hypothesis!= share_premise:
    # check if the share amount in the hypothesis contradicts the share amount reported in the premise
    label = "contradiction"
else:
    # if the share amounts are equal, we can infer entailment
    label = "entailment"

print(label)
