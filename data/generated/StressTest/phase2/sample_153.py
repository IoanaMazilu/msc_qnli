# Premise: Fred and Sam are standing 50 miles apart and they start walking in a straight line toward each other at the same time.
# Hypothesis: Fred and Sam are standing less than 70 miles apart and they start walking in a straight line toward each other at the same time.
# Golden Label: entailment

distance_premise = 50
distance_hypothesis = 70

# the hypothesis refers to the initial distance between Fred and Sam mentioned in the premise
if distance_hypothesis < distance_premise:
    # check if the distance in the hypothesis contradicts the distance in the premise
    label = "contradiction"
elif distance_hypothesis == distance_premise:
    # check if the distance in the hypothesis matches the distance in the premise
    label = "entailment"
else:
    # if the distance in the hypothesis does not contradict the one in the premise and does not match it either
    # we can infer a neutral relation
    label = "neutral"

print(label)
