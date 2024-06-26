distance_premise = 500
distance_hypothesis = 500
speed = 15

# the hypothesis refers to the time Sandy takes to cover a distance, which is also mentioned in the premise
if distance_hypothesis <= distance_premise:
    # check if the hypothesis value contradicts the premise distance
    label = "contradiction"
else:
    # the premise gives an exact distance, so any distance greater than 'distance_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
