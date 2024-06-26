start_floor_premise = 11
start_floor_hypothesis = 51
rate_premise = 87
rate_hypothesis = 87

# the hypothesis refers to the floor and rate at which Steve gets on the elevator, mentioned also in the premise
if start_floor_hypothesis < start_floor_premise:
    # check if the floor number in the hypothesis contradicts the start floor in the premise
    label = "contradiction"
elif rate_hypothesis != rate_premise:
    # check if the rate in the hypothesis contradicts the rate reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
