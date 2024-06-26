floor_start_premise = 61
floor_start_hypothesis = 11
elevator_speed_premise = 57
elevator_speed_hypothesis = 57

# the hypothesis talks about the floor from which David starts in the elevator and the speed of the elevator, both referenced in the premise as well
if floor_start_hypothesis >= floor_start_premise:
    # check if the hypothesis floor contradicts the premise estimate of less than 'floor_start_premise'
    label = "contradiction"
elif elevator_speed_hypothesis != elevator_speed_premise:
    # check if the elevator speed in the hypothesis contradicts the elevator speed reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the starting floor
    # any floor less than 'floor_start_premise' and 'elevator_speed_premise' is consistent with the premise and can be explicitly entailed from the premise
    label = "entailment"

print(label)
