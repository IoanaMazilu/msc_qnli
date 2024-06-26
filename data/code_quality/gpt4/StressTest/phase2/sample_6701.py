tony_share_premise = 4500
tony_share_hypothesis = 7500

# the hypothesis refers to Tony's share mentioned in the premise
if tony_share_hypothesis != tony_share_premise:
    # check if the value of 'tony_share_hypothesis' contradicts the value of Tony's share in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
