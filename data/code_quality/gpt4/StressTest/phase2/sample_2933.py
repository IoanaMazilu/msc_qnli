distance_premise = 48
distance_hypothesis = 38

# the hypothesis refers to the same distance mentioned in the premise
if distance_hypothesis != distance_premise:
    # check if the distance in the hypothesis contradicts the one reported in the premise
    label = "contradiction"
else:
    # if the hypothesis distance does not contradict the premise distance, we can infer entailment
    label = "entailment"

print(label)
