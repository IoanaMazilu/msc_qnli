amount_premise = 45000
amount_hypothesis = 45000

# the hypothesis mentions the amount of money stolen, which is also mentioned in the premise
if amount_hypothesis!= amount_premise:
    # check if the amount in the hypothesis contradicts the amount reported in the premise
    label = "contradiction"
else:
    # if the amount in the hypothesis does not contradict the amount in the premise, we can infer entailment
    label = "entailment"

print(label)
