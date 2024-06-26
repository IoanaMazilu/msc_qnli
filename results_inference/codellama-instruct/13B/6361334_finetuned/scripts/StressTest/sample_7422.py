albert_elevator_premise = 51
albert_elevator_hypothesis = 61

# the hypothesis refers to the floor at which Albert gets on the elevator, which is also mentioned in the premise
if albert_elevator_hypothesis >= albert_elevator_premise:
    # check if the hypothesis value contradicts the floor number in the premise
    label = "contradiction"
else:
    # the premise gives an estimate for the floor at which Albert gets on the elevator
    # any floor number less than 'albert_elevator_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
