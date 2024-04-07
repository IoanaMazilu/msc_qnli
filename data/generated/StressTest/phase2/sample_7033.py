# Premise: Fred and Sam are standing less than 800 miles apart and they start walking in a straight line toward each other at the same time.
# Hypothesis: Fred and Sam are standing 100 miles apart and they start walking in a straight line toward each other at the same time.
# Golden Label: neutral

distance_premise = 800
distance_hypothesis = 100

# the hypothesis refers to the initial distance between Fred and Sam, also mentioned in the premise
if distance_hypothesis > distance_premise:
    # check if the initial distance in the hypothesis contradicts the estimate of less than 'distance_premise' miles apart
    label = "contradiction"
elif distance_hypothesis < distance_premise:
    # the premise gives only an estimate for the initial distance between Fred and Sam
    # any initial distance less than 'distance_premise' is consistent with the premise, but cannot be explicitly entailed from it
    label = "neutral"
else:
    # if the initial distance in the hypothesis equals the initial distance in the premise, we can infer entailment
    label = "entailment"

print(label)

