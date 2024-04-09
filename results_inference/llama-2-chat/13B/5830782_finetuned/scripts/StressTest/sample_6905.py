payment_premise = 160
payment_hypothesis = 760

# the hypothesis refers to the payment made by Rahul, which is also mentioned in the premise
if payment_premise!= payment_hypothesis:
    # check if the payment value in the hypothesis contradicts the payment value mentioned in the premise
    label = "contradiction"
else:
    # if the payment value in the hypothesis does not contradict the payment value in the premise, we can infer entailment
    label = "entailment"

print(label)
