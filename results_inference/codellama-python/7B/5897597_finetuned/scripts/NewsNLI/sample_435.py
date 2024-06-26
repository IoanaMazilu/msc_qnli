restitution_premise = 860000
restitution_hypothesis = 860000

# the hypothesis mentions the amount of money that Kilpatrick will be required to pay back, which is also mentioned in the premise
if restitution_hypothesis!= restitution_premise:
    # check if the amount of money from the hypothesis contradicts the amount of money in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise value, we can infer entailment
    label = "entailment"

print(label)
