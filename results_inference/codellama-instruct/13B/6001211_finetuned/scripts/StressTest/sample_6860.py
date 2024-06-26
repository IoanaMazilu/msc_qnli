distance_walked_premise = 4
distance_walked_hypothesis = 4

# the hypothesis refers to the distance walked by Jack mentioned in the premise
if distance_walked_hypothesis <= distance_walked_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
else:
    # the premise gives the exact distance walked
    # any distance greater than 'distance_walked_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
