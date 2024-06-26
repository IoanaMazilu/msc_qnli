albert_elevator_premise = 61
albert_elevator_hypothesis = 51
albert_elevator_rate = 63

# the hypothesis refers to the floor number and the rate at which Albert rides the elevator
if albert_elevator_premise <= albert_elevator_hypothesis:
    # check if the estimate of 'albert_elevator_hypothesis' contradicts the floor number in the premise
    label = "contradiction"
elif albert_elevator_rate!= 63:
    # check if the rate at which Albert rides the elevator in the hypothesis contradicts the rate mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
