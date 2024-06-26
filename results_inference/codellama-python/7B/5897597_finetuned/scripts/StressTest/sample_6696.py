amount_withdrawn_premise = 2000
amount_withdrawn_hypothesis = 5000

# the hypothesis refers to the amount Tony withdraws, which is also mentioned in the premise
if amount_withdrawn_premise >= amount_withdrawn_hypothesis:
    # check if the amount Tony withdraws in the premise contradicts the estimate of less than 'amount_withdrawn_hypothesis'
    label = "contradiction"
else:
    # if the premise value does not contradict the hypothesis estimate, we can infer entailment
    label = "entailment"

print(label)
