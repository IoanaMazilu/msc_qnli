# Premise: Fred and Sam are standing less than 65 miles apart and they start walking in a straight line toward each other at the same time.
# Hypothesis: Fred and Sam are standing 55 miles apart and they start walking in a straight line toward each other at the same time.
# Golden Label: neutral

distance_premise = 65
distance_hypothesis = 55

# the hypothesis talks about the distance between Fred and Sam, referenced also in the premise
if distance_hypothesis > distance_premise:
    # check if the distance value in the hypothesis contradicts the estimate of less than 'distance_premise'
    label = "contradiction"
elif distance_hypothesis < distance_premise:
    # the premise gives only an estimate for the distance
    # any distance less than 'distance_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

