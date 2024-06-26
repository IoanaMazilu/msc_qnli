distance_premise = 50
speed_walking_premise = 4
speed_running_premise = 6

distance_hypothesis = 50
speed_walking_hypothesis = 4
speed_running_hypothesis = 6

# the hypothesis refers to the distance between their homes and the walking and running speeds mentioned in the premise
if distance_hypothesis <= distance_premise:
    # check if the hypothesis value contradicts the estimate of more than 'distance_premise'
    label = "contradiction"
elif speed_walking_hypothesis!= speed_walking_premise:
    # check if the walking speed in the hypothesis contradicts the walking speed reported in the premise
    label = "contradiction"
elif speed_running_hypothesis!= speed_running_premise:
    # check if the running speed in the hypothesis contradicts the running speed reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
