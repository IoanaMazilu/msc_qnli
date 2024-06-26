withdrawal_premise = 2000
withdrawal_hypothesis = 7000

# the hypothesis refers to the amount Tony withdraws, which is also mentioned in the premise
if withdrawal_hypothesis!= withdrawal_premise:
    # check if the amount Tony withdraws in the hypothesis contradicts the amount in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
