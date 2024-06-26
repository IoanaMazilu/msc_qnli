withdraw_premise = 2000
withdraw_hypothesis = 5000

# the hypothesis refers to the amount Tony withdraws, which is also mentioned in the premise
if withdraw_premise >= withdraw_hypothesis:
    # check if the amount Tony withdraws in the premise contradicts the estimate of less than 'withdraw_hypothesis'
    label = "contradiction"
elif withdraw_premise < withdraw_hypothesis:
    # if the amount Tony withdraws in the premise is less than 'withdraw_hypothesis', it can be inferred entailment
    label = "entailment"
else:
    # if the amount Tony withdraws in the premise is equal to 'withdraw_hypothesis', it is neutral
    label = "neutral"

print(label)
