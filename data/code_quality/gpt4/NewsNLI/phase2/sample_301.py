down_payment_premise = 10000
down_payment_hypothesis = 10000

# the hypothesis mentions the down payment which is also mentioned in the premise
if down_payment_hypothesis != down_payment_premise:
    # check if the down payment in the hypothesis contradicts the down payment reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
