# Premise: The distance from Steve's house to work is 30 Km.
# Hypothesis: The distance from Steve's house to work is 70 Km.
# Golden Label: contradiction

distance_premise = 30
distance_hypothesis = 70

# The hypothesis refers to the same distance mentioned in the premise
if distance_premise != distance_hypothesis:
    # Check if the distance in the hypothesis contradicts the distance reported in the premise
    label = "contradiction"
else:
    # If the distance in the hypothesis and premise are the same, we can infer entailment
    label = "entailment"

print(label)

