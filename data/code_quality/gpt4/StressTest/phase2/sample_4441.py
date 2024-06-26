floor_number_premise = 81
floor_number_hypothesis = 61
speed_premise = 78
speed_hypothesis = 78

# the hypothesis talks about the floor Joyce starts her ride and the speed of the elevator, both also mentioned in the premise
if floor_number_hypothesis >= floor_number_premise:
    # check if the floor number in the hypothesis contradicts the estimate of less than 'floor_number_premise' floors
    label = "contradiction"
elif speed_hypothesis != speed_premise:
    # check if the speed of the elevator in the hypothesis contradicts the speed reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
