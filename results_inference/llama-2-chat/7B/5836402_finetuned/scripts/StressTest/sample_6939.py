floor_premise = 51
floor_hypothesis = 61
speed_premise = 63
speed_hypothesis = 63

# the hypothesis refers to the floor and speed of the elevator mentioned in the premise
if floor_hypothesis >= floor_premise:
    # check if the estimate of 'floor_hypothesis' contradicts the floor number in the premise
    label = "contradiction"
elif speed_hypothesis!= speed_premise:
    # check if the speed in the hypothesis contradicts the speed reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
