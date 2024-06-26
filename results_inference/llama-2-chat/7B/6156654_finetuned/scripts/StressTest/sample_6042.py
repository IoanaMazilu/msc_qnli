distance_premise = 40
distance_hypothesis = 10
speed_premise = 4
speed_hypothesis = 4
speed_running_premise = 6
speed_running_hypothesis = 6

# the hypothesis talks about the distance between their homes, Maxwell's walking speed, and Brad's running speed
if distance_premise <= distance_hypothesis:
    # check if the distance in the hypothesis contradicts the distance in the premise
    label = "contradiction"
elif speed_premise!= speed_hypothesis or speed_running_premise!= speed_running_hypothesis:
    # check if the walking or running speed in the hypothesis contradicts the speed in the premise
    label = "contradiction"
else:
    # if the hypothesis values and premise values do not contradict, we can infer entailment
    label = "entailment"

print(label)
