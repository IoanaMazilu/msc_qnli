restitution_premise = 860000
restitution_hypothesis = 860000

# the hypothesis mentions the amount of restitution to be paid back, which is also mentioned in the premise
if restitution_hypothesis!= restitution_premise:
    # check if the amount of restitution in the hypothesis contradicts the amount in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
