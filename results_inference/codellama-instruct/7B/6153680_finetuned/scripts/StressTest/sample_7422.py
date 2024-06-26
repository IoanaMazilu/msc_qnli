elevator_floor_premise = 51
elevator_floor_hypothesis = 61
elevator_rate_premise = 63
elevator_rate_hypothesis = 63

# the hypothesis refers to the same elevator ride as the premise, but with a different floor
if elevator_floor_hypothesis >= elevator_floor_premise:
    # check if the hypothesis floor contradicts the premise
    label = "contradiction"
elif elevator_rate_hypothesis!= elevator_rate_premise:
    # check if the hypothesis rate contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
