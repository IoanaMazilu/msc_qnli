compensation_premise = 220000
compensation_hypothesis = 220000

# the hypothesis mentions the compensation amount for families of the deceased and victims with debilitating damage, which is also mentioned in the premise
if compensation_hypothesis!= compensation_premise:
    # check if the compensation amount in the hypothesis contradicts the compensation amount reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
