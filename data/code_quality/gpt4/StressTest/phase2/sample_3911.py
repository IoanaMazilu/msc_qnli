distance_premise = 360
distance_hypothesis = 860

# the hypothesis refers to the distance between Jack and Christina mentioned in the premise
if distance_hypothesis != distance_premise:
    # check if the distance in the hypothesis contradicts the distance reported in the premise
    label = "contradiction"
else:
    # the distances in the premise and hypothesis are the same
    label = "entailment"

print(label)
