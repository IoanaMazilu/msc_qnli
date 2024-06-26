share_tony_premise = 4500
share_tony_hypothesis = 7500

# the hypothesis refers to the share of Tony mentioned in the premise
if share_tony_hypothesis!= share_tony_premise:
    # check if the share of Tony in the hypothesis contradicts the share of Tony in the premise
    label = "contradiction"
else:
    # if the share of Tony in the hypothesis matches the share of Tony in the premise, we can infer entailment
    label = "entailment"

print(label)
