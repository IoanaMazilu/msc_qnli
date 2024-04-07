# Premise: Fred and Sam are standing 55 miles apart and they start walking in a straight line toward each other at the same time.
# Hypothesis: Fred and Sam are standing less than 55 miles apart and they start walking in a straight line toward each other at the same time.
# Golden Label: contradiction

distance_premise = 55
distance_hypothesis = 55

# the hypothesis talks about the initial distance between Fred and Sam, also mentioned in the premise
if distance_hypothesis >= distance_premise:
    # check if the distance in the hypothesis contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis distance is less than the premise one, it cannot be entailed from the premise
    label = "neutral"

print(label)

