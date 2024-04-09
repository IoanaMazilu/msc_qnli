discount_premise = 20
discount_hypothesis = 30
payment_premise = 4

# the hypothesis refers to the discount rate and the payment amount mentioned in the premise
if discount_hypothesis <= discount_premise:
    # check if the estimate of 'discount_hypothesis' contradicts the discount rate in the premise
    label = "contradiction"
elif payment_premise!= payment_hypothesis:
    # check if the payment amount in the hypothesis contradicts the payment amount reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
