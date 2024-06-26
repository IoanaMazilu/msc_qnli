withdrawal_amount_premise = 14000
withdrawal_amount_hypothesis = 14000
withdrawal_months_premise = 8
withdrawal_months_hypothesis = 8

# the hypothesis refers to the withdrawal amount and months mentioned in the premise
if withdrawal_amount_premise >= withdrawal_amount_hypothesis:
    # check if the estimate of 'withdrawal_amount_hypothesis' contradicts the withdrawal amount in the premise
    label = "contradiction"
elif withdrawal_months_hypothesis!= withdrawal_months_premise:
    # check if the number of withdrawal months in the hypothesis contradicts the number of withdrawal months reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
