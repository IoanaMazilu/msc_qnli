total_amount_premise = 600
greg_share_premise = "Rs."
greg_share_hypothesis = "Rs."

# the hypothesis refers to the amount and Greg's share mentioned in the premise
if total_amount_premise!= total_amount_hypothesis:
    # check if the total amount in the hypothesis contradicts the total amount reported in the premise
    label = "contradiction"
elif greg_share_premise!= greg_share_hypothesis:
    # check if Greg's share in the hypothesis contradicts Greg's share reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
