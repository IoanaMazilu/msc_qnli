distance_1_premise = 3
distance_1_hypothesis = 8
speed_1 = 40
stop_time = 12
distance_2 = 20
speed_2 = 60

# the hypothesis refers to the distances travelled by Jerry, mentioned in the premise, at the same average speeds
if distance_1_hypothesis <= distance_1_premise:
    # check if the distance travelled at the first speed in the hypothesis contradicts the premise estimate of more than 'distance_1_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the first distance travelled
    # the hypothesis value for the first distance travelled is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
