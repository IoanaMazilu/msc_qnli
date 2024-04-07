# Premise: Jack and Christina are standing 270 feet apart on a level surface.
# Hypothesis: Jack and Christina are standing 570 feet apart on a level surface.
# Golden Label: contradiction

distance_premise = 270
distance_hypothesis = 570

# The hypothesis refers to the distance between Jack and Christina mentioned in the premise
if distance_premise != distance_hypothesis:
    # check if the distance in the hypothesis contradicts the distance reported in the premise
    label = "contradiction"
else:
    # if the distance in the hypothesis does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)

