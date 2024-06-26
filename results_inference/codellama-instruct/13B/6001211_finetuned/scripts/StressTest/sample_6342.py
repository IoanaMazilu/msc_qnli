premise_amount = 288
hypothesis_amount = 588

# the hypothesis refers to the amount mentioned in the premise
if premise_amount >= hypothesis_amount:
    # check if the premise amount contradicts the estimate of 'less than hypothesis_amount'
    label = "contradiction"
else:
    # if the premise amount does not contradict the hypothesis estimate, we can infer entailment
    label = "entailment"

print(label)
