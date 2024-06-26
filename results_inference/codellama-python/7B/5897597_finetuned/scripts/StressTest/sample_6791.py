distance_premise = 50
distance_hypothesis = 50
maxwell_speed_premise = 4
maxwell_speed_hypothesis = 4
brad_speed_premise = 6
brad_speed_hypothesis = 6

# the hypothesis refers to the distance between homes, Maxwell's walking speed and Brad's running speed mentioned in the premise
if distance_hypothesis <= distance_premise:
    # check if the estimate of 'distance_hypothesis' contradicts the distance in the premise
    label = "contradiction"
elif maxwell_speed_hypothesis!= maxwell_speed_premise:
    # check if the Maxwell's walking speed in the hypothesis contradicts the speed reported in the premise
    label = "contradiction"
elif brad_speed_hypothesis!= brad_speed_premise:
    # check if the Brad's running speed in the hypothesis contradicts the speed reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
