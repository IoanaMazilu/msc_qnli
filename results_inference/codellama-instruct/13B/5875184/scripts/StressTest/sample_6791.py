distance_premise = 50
distance_hypothesis = 50
maxwell_walking_speed = 4
brad_running_speed = 6

# the hypothesis refers to the distance between their homes, which is mentioned in the premise
if distance_hypothesis <= distance_premise:
    # check if the estimate of 'distance_hypothesis' contradicts the number of kilometers mentioned in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the distance between their homes
    # any distance greater than 'distance_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
