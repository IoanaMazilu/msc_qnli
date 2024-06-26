start_floor_premise = 11
start_floor_hypothesis = 41
rate_premise = 72
rate_hypothesis = 72

# the hypothesis refers to the floor Steve gets on the elevator, and the rate of riding, both mentioned also in the premise
if start_floor_hypothesis <= start_floor_premise:
    # check if the hypothesis value contradicts the exact floor mentioned in the premise
    label = "contradiction"
elif rate_premise != rate_hypothesis:
    # check if the riding rate in the hypothesis contradicts the riding rate reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
