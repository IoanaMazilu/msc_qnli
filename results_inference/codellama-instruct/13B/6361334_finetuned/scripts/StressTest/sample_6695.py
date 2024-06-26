withdrawal_premise = 14000
withdrawal_hypothesis = 14000
months_premise = 8
months_hypothesis = 8

# the hypothesis refers to the withdrawal amount and the number of months mentioned in the premise
if withdrawal_hypothesis <= withdrawal_premise:
    # check if the estimate of 'withdrawal_hypothesis' contradicts the withdrawal amount in the premise
    label = "contradiction"
elif months_hypothesis!= months_premise:
    # check if the number of months in the hypothesis contradicts the number of months reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
