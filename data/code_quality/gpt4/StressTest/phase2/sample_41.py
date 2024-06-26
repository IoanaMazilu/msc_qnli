distance_premise = 40
distance_hypothesis = 10

# the hypothesis refers to the distance from Marathon to Athens mentioned in the premise
if distance_hypothesis != distance_premise:
    # check if the distance in the hypothesis contradicts the distance reported in the premise
    label = "contradiction"
else:
    # if the distance in the hypothesis and premise are the same, we can infer entailment
    label = "entailment"

print(label)
