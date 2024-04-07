# Premise: Fred and Sam are standing 35 miles apart and they start walking in a straight line toward each other at the same time.
# Hypothesis: Fred and Sam are standing more than 35 miles apart and they start walking in a straight line toward each other at the same time.
# Golden Label: contradiction

distance_premise = 35
distance_hypothesis = 35

# the hypothesis refers to the distance between Fred and Sam mentioned in the premise
if distance_hypothesis > distance_premise:
    # check if the distance in the hypothesis contradicts the distance reported in the premise
    label = "contradiction"
else:
    # if the distance in the hypothesis does not contradict the distance in the premise, we can infer entailment
    label = "entailment"

print(label)

