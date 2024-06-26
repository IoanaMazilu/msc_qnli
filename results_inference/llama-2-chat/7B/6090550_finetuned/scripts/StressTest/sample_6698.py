ymetal_premise = 2000
ymetal_hypothesis = 7000

# the hypothesis mentions the amount Tony withdraws, which is also referenced in the premise
if ymetal_hypothesis!= ymetal_premise:
    # check if the amount in the hypothesis contradicts the amount in the premise
    label = "contradiction"
else:
    # if the amounts are the same, we can infer entailment
    label = "entailment"

print(label)
