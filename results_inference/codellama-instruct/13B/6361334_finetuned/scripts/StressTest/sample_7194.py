distance_premise = 7
distance_hypothesis = 6

# the hypothesis refers to the time required to cover the distance between Chennai and Jammu, mentioned in the premise
if distance_hypothesis <= distance_premise:
    # check if the estimate of 'distance_hypothesis' contradicts the time required in the premise
    label = "contradiction"
else:
    # the premise gives an exact time required to cover the distance
    # any time greater than 'distance_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
