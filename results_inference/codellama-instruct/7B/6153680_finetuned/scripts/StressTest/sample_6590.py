elevator_floor_premise = 11
elevator_floor_hypothesis = 71
elevator_rate_premise = 87
elevator_rate_hypothesis = 87

# the hypothesis refers to the same elevator ride as the premise, but with a different floor
if elevator_floor_hypothesis!= elevator_floor_premise:
    label = "contradiction"
elif elevator_rate_hypothesis!= elevator_rate_premise:
    label = "contradiction"
else:
    label = "entailment"

print(label)
