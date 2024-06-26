floor_premise = 11
floor_hypothesis = 61
speed_premise = 57
speed_hypothesis = 57

# the hypothesis talks about the floor and speed of the elevator, which are also mentioned in the premise
if floor_hypothesis <= floor_premise:
    # check if the hypothesis value contradicts the floor value in the premise
    label = "contradiction"
elif speed_hypothesis!= speed_premise:
    # check if the speed value in the hypothesis contradicts the speed value in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
