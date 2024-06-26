distance_premise = 15
distance_hypothesis = 15

# the hypothesis talks about the distance between two towns, referenced also in the premise
if distance_hypothesis <= distance_premise:
    # check if the hypothesis value contradicts the distance in the premise
    label = "contradiction"
else:
    # the premise gives a specific distance
    # any distance greater than 'distance_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
