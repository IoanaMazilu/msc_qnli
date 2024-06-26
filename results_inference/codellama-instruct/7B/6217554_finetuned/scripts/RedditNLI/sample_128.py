payment_premise = 7.2
payment_hypothesis = 7.15

# the hypothesis and premise mention the payment amount
if payment_hypothesis!= payment_premise:
    # check if the payment amount in the hypothesis contradicts the payment amount in the premise
    label = "contradiction"
else:
    # if the payment amount in the hypothesis does not contradict the payment amount in the premise, we can infer entailment
    label = "entailment"

print(label)
