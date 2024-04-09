distance_premise = 45
distance_hypothesis = 45

# the hypothesis refers to the same distance mentioned in the premise
if distance_hypothesis <= distance_premise:
    # check if the hypothesis value contradicts the premise
    label = "contradiction"
else:
    # the premise gives an exact distance
    # any distance greater than 'distance_premise' contradicts the premise
    label = "contradiction"

print(label)
