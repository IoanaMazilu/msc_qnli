floor_premise = 51
floor_hypothesis = 71
speed_premise = 93
speed_hypothesis = 93

# the hypothesis talks about the floor and speed of the elevator ride mentioned in the premise
if floor_hypothesis <= floor_premise:
    # check if the hypothesis value contradicts the estimate of more than 'floor_premise'
    label = "contradiction"
elif speed_hypothesis!= speed_premise:
    # check if the speed of the elevator ride in the hypothesis contradicts the speed reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the floor
    # any floor greater than 'floor_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
