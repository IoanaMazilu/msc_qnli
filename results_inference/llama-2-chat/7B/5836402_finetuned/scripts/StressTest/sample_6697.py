withdrawal_premise = 5000
withdrawal_hypothesis = 2000

# the hypothesis refers to the amount Tony withdraws, mentioned in the premise
if withdrawal_hypothesis >= withdrawal_premise:
    # check if the amount Tony withdraws in the hypothesis contradicts the estimate of less than 'withdrawal_premise'
    label = "contradiction"
else:
    # if the amount Tony withdraws in the hypothesis does not contradict the premise estimate, we can infer entailment
    label = "entailment"

print(label)
