# Premise: Fred and Sam are standing less than 45 miles apart and they start walking in a straight line toward each other at the same time.
# Hypothesis: Fred and Sam are standing 35 miles apart and they start walking in a straight line toward each other at the same time.
# Golden Label: neutral

distance_premise = 45
distance_hypothesis = 35

# the hypothesis refers to the distance between Fred and Sam mentioned in the premise
if distance_hypothesis > distance_premise:
    # check if the 'distance_hypothesis' contradicts the maximum distance given in the premise
    label = "contradiction"
elif distance_hypothesis < distance_premise:
    # check if the 'distance_hypothesis' is less than the maximum distance given in the premise
    # the premise gives only an upper limit for the distance
    # any distance less than 'distance_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"
else:
    # if the 'distance_hypothesis' is equal to the 'distance_premise', we can infer entailment
    label = "entailment"

print(label)

