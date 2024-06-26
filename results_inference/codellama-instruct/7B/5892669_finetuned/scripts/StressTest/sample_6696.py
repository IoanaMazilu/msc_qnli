withdraw_premise = 2000
withdraw_hypothesis = 5000

# the hypothesis refers to the amount Tony withdraws, which is also mentioned in the premise
if withdraw_premise >= withdraw_hypothesis:
    # check if the premise value contradicts the estimate of less than 'withdraw_hypothesis'
    label = "contradiction"
else:
    # if the premise value does not contradict the hypothesis estimate, we can infer entailment
    label = "entailment"

print(label)
