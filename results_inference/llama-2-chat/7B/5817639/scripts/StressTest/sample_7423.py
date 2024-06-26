floor_premise = 61
floor_hypothesis = 51
elevator_rate_premise = 63
elevator_rate_hypothesis = 63

# the hypothesis refers to the floor and elevator rate mentioned in the premise
if floor_hypothesis <= floor_premise:
    # check if the hypothesis value contradicts the estimate of 'floor_premise'
    label = "contradiction"
elif elevator_rate_hypothesis!= elevator_rate_premise:
    # check if the number of floors in the hypothesis contradicts the number of floors reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
