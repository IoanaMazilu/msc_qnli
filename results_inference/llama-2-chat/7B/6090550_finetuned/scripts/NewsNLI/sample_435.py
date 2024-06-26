restitution_premise = 860000
restitution_hypothesis = 860000

# the hypothesis mentions the amount of restitution that Kilpatrick will be required to pay back, which is also mentioned in the premise
if restitution_hypothesis!= restitution_premise:
    # check if the restitution amount in the hypothesis contradicts the restitution amount in the premise
    label = "contradiction"
else:
    # if the restitution amount in the hypothesis matches the restitution amount in the premise, we can infer entailment
    label = "entailment"

print(label)
