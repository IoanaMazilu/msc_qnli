floor_premise = 51
floor_hypothesis = 81
elevator_rate_premise = 63
elevator_rate_hypothesis = 63

# the hypothesis talks about the floor and elevator rate, both referenced in the premise
if floor_hypothesis <= floor_premise:
    # check if the hypothesis value contradicts the estimate of the same floor in the premise
    label = "contradiction"
elif elevator_rate_hypothesis!= elevator_rate_premise:
    # check if the hypothesis value contradicts the estimate of the elevator rate in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
