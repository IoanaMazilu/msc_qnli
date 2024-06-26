withdrawal_premise = 14000
withdrawal_hypothesis = 44000

# the hypothesis refers to the amount of money withdrawn by John after 8 months
if withdrawal_hypothesis <= withdrawal_premise:
    # check if the hypothesis value contradicts the estimate of 'withdrawal_premise'
    label = "contradiction"
elif withdrawal_hypothesis!= withdrawal_premise:
    # check if the hypothesis value contradicts the amount of money withdrawn in the premise
    label = "contradiction"
else:
    # if the hypothesis value and estimate do not contradict the premise, we can infer entailment
    label = "entailment"

print(label)
