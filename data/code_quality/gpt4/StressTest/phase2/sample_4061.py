distance_homes_premise = 36
distance_homes_hypothesis = 36
betty_speed_premise = 4
betty_speed_hypothesis = 4
dave_speed_premise = 3
dave_speed_hypothesis = 3

# the hypothesis refers to the distance between homes and both Betty's and Dave's walking speeds
if distance_homes_hypothesis >= distance_homes_premise:
    # check if the estimate of 'distance_homes_hypothesis' contradicts the distance mentioned in the premise
    label = "contradiction"
elif betty_speed_hypothesis != betty_speed_premise:
    # check if the number of betty's speed in the hypothesis contradicts the speed mentioned in the premise
    label = "contradiction"
elif dave_speed_hypothesis != dave_speed_premise:
    # check if the number of dave's speed in the hypothesis contradicts the speed mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
