# Premise: The Panamanian-flagged carrier, the'' Danny F II,'' sank about 12 miles off the coast of Tripoli.
# Hypothesis: Panamanian-flagged ship sinks about 12 miles off the coast of Tripoli.
# Golden Label: entailment

distance_premise = 12
distance_hypothesis = 12

# the hypothesis mentions the distance where the ship sank, which is also mentioned in the premise
if distance_hypothesis != distance_premise:
    # check if the distance in the hypothesis contradicts the distance reported in the premise
    label = "contradiction"
else:
    # if the hypothesis distance does not contradict the premise distance, we can infer entailment
    label = "entailment"

print(label)

