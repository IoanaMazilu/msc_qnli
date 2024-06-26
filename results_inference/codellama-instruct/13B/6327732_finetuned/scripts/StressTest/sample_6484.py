distance_premise = 80
distance_hypothesis = 20
maxwell_walking_speed_premise = 4
maxwell_walking_speed_hypothesis = 4
brad_running_speed_premise = 6
brad_running_speed_hypothesis = 6

# the hypothesis refers to the distance between their homes and the walking speed of Maxwell
if distance_hypothesis <= distance_premise:
    # check if the estimate of 'distance_hypothesis' contradicts the distance in the premise
    label = "contradiction"
elif maxwell_walking_speed_hypothesis!= maxwell_walking_speed_premise:
    # check if the walking speed of Maxwell in the hypothesis contradicts the walking speed mentioned in the premise
    label = "contradiction"
elif brad_running_speed_hypothesis!= brad_running_speed_premise:
    # check if the running speed of Brad in the hypothesis contradicts the running speed mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
