# Premise: 4500 find the share of Tony.
# Hypothesis: less than 6500 find the share of Tony.
# Golden Label: entailment

tony_share_premise = 4500
tony_share_hypothesis = 6500

# the hypothesis refers to Tony's share mentioned in the premise
if tony_share_premise >= tony_share_hypothesis:
    # check if the estimate of 'tony_share_hypothesis' contradicts the number of Tony's share in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

