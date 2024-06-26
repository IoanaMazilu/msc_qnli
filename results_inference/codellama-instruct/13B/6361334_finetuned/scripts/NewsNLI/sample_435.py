restitution_premise = 860000
restitution_hypothesis = 860000

# the hypothesis mentions the amount of restitution that Kilpatrick will be required to pay back, which is also mentioned in the premise
if restitution_hypothesis!= restitution_premise:
    # check if the amount of restitution in the hypothesis contradicts the amount of restitution in the premise
    label = "contradiction"
else:
    # if the amount of restitution in the hypothesis does not contradict the amount of restitution in the premise, we can infer entailment
    label = "entailment"

print(label)
