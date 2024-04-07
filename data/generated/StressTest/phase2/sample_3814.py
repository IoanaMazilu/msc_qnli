# Premise: Fred and Sam are standing less than 60 miles apart and they start walking in a straight line toward each other at the same time.
# Hypothesis: Fred and Sam are standing 40 miles apart and they start walking in a straight line toward each other at the same time.
# Golden Label: neutral

distance_premise = 60
distance_hypothesis = 40

# the hypothesis speaks about the initial distance between Fred and Sam, also mentioned in the premise
if distance_hypothesis > distance_premise:
    # check if the initial distance in the hypothesis contradicts the estimate in the premise
    label = "contradiction"
elif distance_hypothesis < distance_premise:
    # any distance less than 'distance_premise' is consistent with the premise, but cannot be explicitly entailed from it
    label = "neutral"

print(label)

