floor_premise = 61
floor_hypothesis = 11
speed_premise = 57
speed_hypothesis = 57

# the hypothesis talks about the floor and speed of the elevator, referenced also in the premise
if floor_hypothesis <= floor_premise:
    # check if the hypothesis value contradicts the estimate of more than 'floor_premise'
    label = "contradiction"
elif speed_hypothesis!= speed_premise:
    # check if the number of floors in the hypothesis contradicts the number of floors reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
