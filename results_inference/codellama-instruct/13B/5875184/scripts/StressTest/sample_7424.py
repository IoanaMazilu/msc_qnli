elevator_rate_premise = 63
elevator_rate_hypothesis = 63
albert_floor_premise = 51
albert_floor_hypothesis = 81

# the hypothesis refers to the same elevator rate and building as the premise
if elevator_rate_premise == elevator_rate_hypothesis:
    # check if the hypothesis value contradicts the estimate of the same elevator rate in the premise
    label = "contradiction"
elif albert_floor_hypothesis!= albert_floor_premise:
    # check if the hypothesis value contradicts the estimate of the same building in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
