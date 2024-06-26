amount_premise = 750
amount_hypothesis = 450

# the hypothesis refers to the amount sold, which is also mentioned in the premise
if amount_hypothesis >= amount_premise:
    # check if the amount in the hypothesis contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis amount does not contradict the premise amount, we can infer entailment
    label = "entailment"

print(label)
