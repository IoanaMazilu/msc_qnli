# Premise: Fred and Sam are standing 100 miles apart and they start walking in a straight line toward each other at the same time.
# Hypothesis: Fred and Sam are standing more than 100 miles apart and they start walking in a straight line toward each other at the same time.
# Golden Label: contradiction

distance_premise = 100
distance_hypothesis = 100

# the hypothesis talks about the distance between Fred and Sam, referenced also in the premise
if distance_hypothesis > distance_premise:
    # check if the distance in the hypothesis contradicts the distance stated in the premise
    label = "contradiction"
elif distance_hypothesis == distance_premise:
    # if the distance in the hypothesis is the same as in the premise, we can infer entailment
    label = "entailment"
else:
    # any distance less than 'distance_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

