floor_premise = 71
floor_hypothesis = 31
speed_premise = 93
speed_hypothesis = 93

# the hypothesis talks about the floor number and the elevator speed at the same time, referenced also in the premise
if floor_hypothesis!= floor_premise:
    # check if the hypothesis value contradicts the floor number in the premise
    label = "contradiction"
elif speed_hypothesis!= speed_premise:
    # check if the speed of the elevator in the hypothesis contradicts the speed of the elevator reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
