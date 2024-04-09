floor_premise = 51
floor_hypothesis = 31
elevator_rate_premise = 63
elevator_rate_hypothesis = 63

# the hypothesis refers to the floor and elevator rate mentioned in the premise
if floor_hypothesis == floor_premise:
    # check if the estimate of 'floor_hypothesis' contradicts the number of floor mentioned in the premise
    label = "contradiction"
elif elevator_rate_hypothesis!= elevator_rate_premise:
    # check if the number of elevator rate in the hypothesis contradicts the number of elevator rate reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
