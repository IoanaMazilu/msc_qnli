matthew_wake_premise = "t"
matthew_wake_hypothesis = "y"
johnny_walk_premise = "y"
johnny_walk_hypothesis = "t"
distance_premise = 45
distance_hypothesis = 45

# the hypothesis refers to the distance between two points, mentioned in the premise
if distance_hypothesis <= distance_premise:
    # check if the estimate of 'distance_hypothesis' contradicts the distance in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the distance
    # any distance greater than 'distance_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
