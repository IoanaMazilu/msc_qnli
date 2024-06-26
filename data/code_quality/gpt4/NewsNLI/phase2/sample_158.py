distance_premise = 120
distance_hypothesis = 120

# the hypothesis mentions the distance into the sea, which is also referenced in the premise
if distance_hypothesis != distance_premise:
    # check if the distance in the hypothesis contradicts the distance in the premise
    label = "contradiction"
else:
    # if the distance in the hypothesis does not contradict the distance in the premise, we can infer entailment
    label = "entailment"

print(label)
