withdraw_premise = 14000
withdraw_hypothesis = 44000

# the hypothesis refers to the amount John withdraws after 8 months, mentioned in the premise
if withdraw_premise >= withdraw_hypothesis:
    # check if the amount in the premise contradicts the estimate of less than 'withdraw_hypothesis'
    label = "contradiction"
elif withdraw_premise < withdraw_hypothesis:
    # if the premise amount is less than the hypothesis estimate, we can infer entailment
    label = "entailment"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
