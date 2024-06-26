withdraw_premise = 2000
withdraw_hypothesis = 7000

# the hypothesis refers to the amount Tony withdraws, also mentioned in the premise
if withdraw_premise!= withdraw_hypothesis:
    # check if the withdrawal amount in the hypothesis contradicts the withdrawal amount reported in the premise
    label = "contradiction"
else:
    # if the hypothesis amount does not contradict the premise amount, we can infer entailment
    label = "entailment"

print(label)
