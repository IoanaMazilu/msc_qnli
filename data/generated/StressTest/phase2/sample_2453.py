# Premise: Jack and Christina are standing 240 feet apart on a level surface.
# Hypothesis: Jack and Christina are standing 640 feet apart on a level surface.
# Golden Label: contradiction

distance_apart_premise = 240
distance_apart_hypothesis = 640

# the hypothesis refers to the distance between Jack and Christina mentioned in the premise
if distance_apart_hypothesis != distance_apart_premise:
    # check if the distance in the hypothesis contradicts the distance reported in the premise
    label = "contradiction"
else:
    # the hypothesis value and premise value are the same, we can infer entailment
    label = "entailment"

print(label)

