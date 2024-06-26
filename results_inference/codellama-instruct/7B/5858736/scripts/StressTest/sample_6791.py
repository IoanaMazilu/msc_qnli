distance_home_premise = 50
walking_speed_premise = 4
running_speed_premise = 6

# the hypothesis refers to the distance traveled by Brad, which is a function of the distance between their homes and their speeds
if distance_home_premise <= distance_home_hypothesis:
    # check if the estimate of 'distance_home_hypothesis' contradicts the distance between their homes in the premise
    label = "contradiction"
elif walking_speed_premise <= walking_speed_hypothesis:
    # check if the estimate of 'walking_speed_hypothesis' contradicts the walking speed in the premise
    label = "contradiction"
elif running_speed_premise <= running_speed_hypothesis:
    # check if the estimate of 'running_speed_hypothesis' contradicts the running speed in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
