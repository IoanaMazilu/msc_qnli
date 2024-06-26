premise_amount = 220000
hypothesis_amount = 220000

# the hypothesis mentions the same amount as the premise
if hypothesis_amount!= premise_amount:
    # check if the amount in the hypothesis contradicts the amount in the premise
    label = "contradiction"
else:
    # if the amount in the hypothesis does not contradict the amount in the premise, we can infer entailment
    label = "entailment"

print(label)
