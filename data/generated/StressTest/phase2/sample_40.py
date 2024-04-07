# Premise: A runner runs the more than 20 miles from Marathon to Athens at a constant speed.
# Hypothesis: A runner runs the 40 miles from Marathon to Athens at a constant speed.
# Golden Label: neutral

distance_premise = 20
distance_hypothesis = 40

# the hypothesis refers to the distance from Marathon to Athens mentioned in the premise
if distance_hypothesis <= distance_premise:
    # check if the distance in the hypothesis contradicts the estimate of more than 'distance_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the distance
    # any distance greater than 'distance_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

