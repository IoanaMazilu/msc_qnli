distance_premise = 40
distance_hypothesis = 80
walking_speed_premise = 4
walking_speed_hypothesis = 4
running_speed_premise = 6
running_speed_hypothesis = 6

# the hypothesis talks about the distance between their homes, Maxwell's walking speed, and Brad's running speed, which are also mentioned in the premise
if distance_premise!= distance_hypothesis:
    # check if the distance between their homes in the hypothesis contradicts the distance in the premise
    label = "contradiction"
elif walking_speed_premise!= walking_speed_hypothesis or running_speed_premise!= running_speed_hypothesis:
    # check if the walking or running speed in the hypothesis contradicts the speed in the premise
    label = "contradiction"
else:
    # if the distances and speeds in the hypothesis do not contradict the ones in the premise, we can infer entailment
    label = "entailment"

print(label)
