# Premise: Fred and Sam are standing 35 miles apart and they start walking in a straight line toward each other at the same time.
# Hypothesis: Fred and Sam are standing less than 45 miles apart and they start walking in a straight line toward each other at the same time.
# Golden Label: entailment

distance_premise = 35
distance_hypothesis = 45

# the hypothesis refers to the distance between Fred and Sam mentioned in the premise
if distance_premise > distance_hypothesis:
    # check if the 'distance_premise' contradicts the distance in the hypothesis
    label = "contradiction"
elif distance_premise < distance_hypothesis:
    # if the distance in the premise is less than the distance in the hypothesis, we can infer entailment
    label = "entailment"
else:
    # the premise and hypothesis distances are equal
    label = "neutral"

print(label)

