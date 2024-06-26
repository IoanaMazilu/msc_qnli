distance_premise = 60
distance_hypothesis = 60
maxwell_speed = 4
brad_speed = 6

# the hypothesis refers to the distance between homes, Maxwell's speed, and Brad's speed mentioned in the premise
if distance_hypothesis < distance_premise:
    # check if the value of 'distance_hypothesis' contradicts the number of kilometers in the premise
    label = "contradiction"
else:
    # the premise gives the exact distance, speed of Maxwell and Brad
    # the hypothesis is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
