amount_premise = 450
amount_hypothesis = 750

# the hypothesis refers to the amount sold, which is also mentioned in the premise
if amount_premise >= amount_hypothesis:
    # check if the amount in the premise contradicts the estimate of 'less than amount_hypothesis'
    label = "contradiction"
else:
    # if the premise value does not contradict the hypothesis estimate, we can infer entailment
    label = "entailment"

print(label)
