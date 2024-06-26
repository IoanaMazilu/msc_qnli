David_elevator_premise = 61
David_elevator_hypothesis = 11
David_rate_premise = 57
David_rate_hypothesis = 57

# the hypothesis refers to the floor number and the rate of the elevator mentioned in the premise
if David_elevator_hypothesis >= David_elevator_premise:
    # check if the estimate of 'David_elevator_hypothesis' contradicts the floor number in the premise
    label = "contradiction"
elif David_rate_hypothesis!= David_rate_premise:
    # check if the rate of the elevator in the hypothesis contradicts the rate of the elevator reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
