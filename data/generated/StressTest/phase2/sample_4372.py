# Premise: If John runs in the speed of more than 6 km/hr from his house, in what time will he reach the park which is 300 m long from his house?
# Hypothesis: If John runs in the speed of 9 km/hr from his house, in what time will he reach the park which is 300 m long from his house?
# Golden Label: neutral

speed_premise = 6
speed_hypothesis = 9
distance_premise = 300 / 1000 # converting to km
distance_hypothesis = 300 / 1000 # converting to km

# the hypothesis refers to John's running speed and the distance to the park from his house, both mentioned in the premise
if speed_hypothesis <= speed_premise:
    # check if the speed in the hypothesis contradicts the estimate of more than 'speed_premise'
    label = "contradiction"
elif distance_hypothesis != distance_premise:
    # check if the distance in the hypothesis contradicts the distance mentioned in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the speed
    # any speed greater than 'speed_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

