floor_premise = 71
floor_hypothesis = 51
elevator_speed_premise = 93
elevator_speed_hypothesis = 93

# the hypothesis refers to the number of floors and elevator speed mentioned in the premise
if floor_hypothesis <= floor_premise:
    # check if the estimate of 'floor_hypothesis' contradicts the number of floors in the premise
    label = "contradiction"
elif elevator_speed_hypothesis!= elevator_speed_premise:
    # check if the number of floors in the hypothesis contradicts the number of floors reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
