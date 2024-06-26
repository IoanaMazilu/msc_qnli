distance_premise = 240
distance_hypothesis = 340

# the hypothesis refers to the distance between Jack and Christina, which is also mentioned in the premise
if distance_hypothesis != distance_premise:
    # check if the distance in the hypothesis contradicts the distance reported in the premise
    label = "contradiction"
else:
    # if the distance in the hypothesis does not contradict the distance in the premise, we can infer entailment
    label = "entailment"

print(label)
