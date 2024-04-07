# Premise: Jack and Christina are standing 150 feet apart on a level surface.
# Hypothesis: Jack and Christina are standing 250 feet apart on a level surface.
# Golden Label: contradiction

distance_premise = 150
distance_hypothesis = 250

# the hypothesis refers to the distance between Jack and Christina mentioned in the premise
if distance_hypothesis != distance_premise:
    # check if the distance in the hypothesis contradicts the distance reported in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)

