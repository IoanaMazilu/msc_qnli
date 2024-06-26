distance_premise = 35
distance_hypothesis = 35

# the hypothesis refers to the distance between Fred and Sam mentioned in the premise
if distance_hypothesis <= distance_premise:
    # check if the distance in the hypothesis contradicts the distance in the premise
    label = "contradiction"
else:
    # the premise gives an exact distance for Fred and Sam
    # any distance greater than 'distance_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
