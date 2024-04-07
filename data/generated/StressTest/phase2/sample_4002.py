# Premise: Jack and Christina are standing 150 feet apart on a level surface.
# Hypothesis: Jack and Christina are standing less than 450 feet apart on a level surface.
# Golden Label: entailment

distance_premise = 150
distance_hypothesis = 450

# the hypothesis refers to the distance between Jack and Christina mentioned in the premise
if distance_premise > distance_hypothesis:
    # check if the actual distance contradicts the maximum distance mentioned in the hypothesis
    label = "contradiction"
else:
    # if the actual distance doesn't contradict the hypothesis, we can infer entailment
    label = "entailment"

print(label)

