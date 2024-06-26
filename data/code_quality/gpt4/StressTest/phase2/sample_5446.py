distance_premise = 700
distance_hypothesis = 100
speed_premise = 50
speed_hypothesis = 50

# the hypothesis talks about the distance and speed of a train traveling from Albany to Syracuse, also mentioned in the premise
if distance_hypothesis >= distance_premise:
    # check if the distance in the hypothesis contradicts the estimate of less than 'distance_premise'
    label = "contradiction"
elif speed_hypothesis != speed_premise:
    # check if the speed in the hypothesis contradicts the speed reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the distance
    # a distance less than 'distance_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
