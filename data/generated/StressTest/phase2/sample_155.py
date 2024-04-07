# Premise: Fred and Sam are standing 50 miles apart and they start walking in a straight line toward each other at the same time.
# Hypothesis: Fred and Sam are standing more than 50 miles apart and they start walking in a straight line toward each other at the same time.
# Golden Label: contradiction

distance_premise = 50
distance_hypothesis = 50

# the hypothesis refers to the distance between Fred and Sam, which is also mentioned in the premise
if distance_hypothesis != distance_premise:
    # check if the distance in the hypothesis contradicts the distance reported in the premise
    label = "contradiction"
else:
    # if the distance in the hypothesis and the distance in the premise are the same, we can infer entailment
    label = "entailment"

print(label)

