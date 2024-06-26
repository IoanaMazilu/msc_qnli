death_victim_payment_premise = 220000
death_victim_payment_hypothesis = 220000

# the hypothesis mentions the payment for the families of the deceased and victims with debilitating damage, which is also mentioned in the premise
if death_victim_payment_hypothesis!= death_victim_payment_premise:
    # check if the payment in the hypothesis contradicts the payment reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
