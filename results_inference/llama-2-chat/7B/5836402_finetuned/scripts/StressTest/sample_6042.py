distance_premise = 40
distance_hypothesis = 10
maxwell_walking_speed_premise = 4
maxwell_walking_speed_hypothesis = 4
brad_running_speed_premise = 6
brad_running_speed_hypothesis = 6

# the hypothesis refers to the distance between their homes and the walking and running speeds of Maxwell and Brad mentioned in the premise
if distance_hypothesis <= distance_premise:
    # check if the estimate of 'distance_hypothesis' contradicts the distance between their homes in the premise
    label = "contradiction"
elif maxwell_walking_speed_hypothesis!= maxwell_walking_speed_premise or brad_running_speed_hypothesis!= brad_running_speed_premise:
    # check if the walking or running speed of Maxwell or Brad in the hypothesis contradicts their speed in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
