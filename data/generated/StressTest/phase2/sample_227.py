# Premise: Rasik walked 20 m towards north.
# Hypothesis: Rasik walked 40 m towards north.
# Golden Label: contradiction

distance_walked_premise = 20
distance_walked_hypothesis = 40

# the hypothesis refers to the distance Rasik walked towards north, also mentioned in the premise
if distance_walked_hypothesis != distance_walked_premise:
    # check if the distance reported in the hypothesis contradicts the distance reported in the premise
    label = "contradiction"
else:
    # if the distance walked in the hypothesis does not contradict the distance walked in the premise, we can infer entailment
    label = "entailment"

print(label)

