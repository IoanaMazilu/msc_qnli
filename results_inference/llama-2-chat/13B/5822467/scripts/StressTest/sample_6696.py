withdrawals_premise = 2000
withdrawals_hypothesis = 5000

# the hypothesis refers to the amount of withdrawals mentioned in the premise
if withdrawals_hypothesis <= withdrawals_premise:
    # check if the estimate of 'withdrawals_hypothesis' contradicts the amount of withdrawals in the premise
    label = "contradiction"
elif withdrawals_premise!= withdrawals_hypothesis:
    # check if the amount of withdrawals in the hypothesis contradicts the amount of withdrawals reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
