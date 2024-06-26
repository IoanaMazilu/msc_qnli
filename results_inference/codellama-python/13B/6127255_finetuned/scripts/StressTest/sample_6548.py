distance_premise = 15
distance_hypothesis = 15

# the hypothesis refers to the distance between West-Town to East-Town mentioned in the premise
if distance_hypothesis <= distance_premise:
    # check if the hypothesis value contradicts the distance given in the premise
    label = "contradiction"
else:
    # the premise gives the exact distance
    # any distance greater than 'distance_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
