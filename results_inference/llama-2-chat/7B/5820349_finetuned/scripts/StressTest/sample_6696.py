withdraw_premise = 2000
withdraw_hypothesis = 5000

# the hypothesis refers to the amount Tony withdraws, which is also mentioned in the premise
if withdraw_premise >= withdraw_hypothesis:
    # check if the amount Tony withdraws in the premise contradicts the estimate of less than 'withdraw_hypothesis'
    label = "contradiction"
elif withdraw_premise < withdraw_hypothesis:
    # if the premise amount is less than the hypothesis estimate, we can infer entailment
    label = "entailment"

print(label)
