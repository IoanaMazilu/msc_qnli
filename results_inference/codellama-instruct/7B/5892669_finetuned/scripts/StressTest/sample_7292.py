share_value_premise = 600
share_value_hypothesis = 400

# the hypothesis refers to the value of Greg's share mentioned in the premise
if share_value_hypothesis!= share_value_premise:
    # check if the value of Greg's share in the hypothesis contradicts the value of Greg's share reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
