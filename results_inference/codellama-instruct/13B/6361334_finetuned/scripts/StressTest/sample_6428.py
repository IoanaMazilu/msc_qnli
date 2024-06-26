premise_amount = 450
hypothesis_amount = 750

# the hypothesis refers to the amount sold to George, which is also mentioned in the premise
if hypothesis_amount <= premise_amount:
    # check if the estimate of 'hypothesis_amount' contradicts the amount sold in the premise
    label = "contradiction"
else:
    # if the hypothesis value and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
