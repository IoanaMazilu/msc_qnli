amount_premise = 10000
amount_hypothesis = 10000

# the hypothesis mentions the amount that triggers the need for declaration and proof of source, which is also mentioned in the premise
if amount_hypothesis != amount_premise:
    # check if the amount in the hypothesis contradicts the amount reported in the premise
    label = "contradiction"
else:
    # if the amount in the hypothesis does not contradict the premise, we can infer entailment
    label = "entailment"

print(label)
