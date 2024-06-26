elevator_floor_premise = 51
elevator_floor_hypothesis = 71
elevator_speed_premise = 93
elevator_speed_hypothesis = 93

# the hypothesis talks about the floor number and the elevator speed of the same building and time, referenced also in the premise
if elevator_floor_hypothesis <= elevator_floor_premise:
    # check if the hypothesis value contradicts the estimate of more than 'elevator_floor_premise'
    label = "contradiction"
elif elevator_speed_hypothesis!= elevator_speed_premise:
    # check if the elevator speed in the hypothesis contradicts the elevator speed reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the floor number
    # any floor number greater than 'elevator_floor_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
