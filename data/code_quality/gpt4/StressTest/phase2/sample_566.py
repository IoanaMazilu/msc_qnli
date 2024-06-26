distance_premise = 48
distance_hypothesis = 58

# The hypothesis refers to the same distance from Lionel's house to Walt's house mentioned in the premise
if distance_hypothesis != distance_premise:
    # If the distance in the hypothesis does not match the distance in the premise, it is a contradiction
    label = "contradiction"
else:
    # If the distances match, it is an entailment
    label = "entailment"

print(label)
