amount_premise = 10000
amount_hypothesis = 10000

# the hypothesis mentions an amount that triggers the declaration requirement, which is also mentioned in the premise
if amount_hypothesis!= amount_premise:
    # check if the amount in the hypothesis contradicts the amount reported in the premise
    label = "contradiction"
else:
    # if the hypothesis amount does not contradict the premise amount, we can infer entailment
    label = "entailment"

print(label)
