albert_elevator_premise = 51
albert_elevator_hypothesis = 81
albert_rate_premise = 63
albert_rate_hypothesis = 63

# the hypothesis refers to the floor number and the rate of the elevator mentioned in the premise
if albert_elevator_hypothesis <= albert_elevator_premise:
    # check if the estimate of 'albert_elevator_hypothesis' contradicts the floor number in the premise
    label = "contradiction"
elif albert_rate_hypothesis!= albert_rate_premise:
    # check if the rate of the elevator in the hypothesis contradicts the rate mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
