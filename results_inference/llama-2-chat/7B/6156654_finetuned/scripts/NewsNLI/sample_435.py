restitution_amount_premise = 860000
restitution_amount_hypothesis = 860000

# the hypothesis mentions the amount of restitution to be paid back, which is also mentioned in the premise
if restitution_amount_hypothesis!= restitution_amount_premise:
    # check if the amount of restitution in the hypothesis contradicts the amount of restitution in the premise
    label = "contradiction"
else:
    # if the amount of restitution in the hypothesis matches the amount of restitution in the premise, we can infer entailment
    label = "entailment"

print(label)
