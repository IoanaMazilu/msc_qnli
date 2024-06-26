start_road_premise = 2
start_road_hypothesis = 3

# the hypothesis refers to the starting point of the route mentioned in the premise
if start_road_hypothesis <= start_road_premise:
    # check if the starting point of the route in the hypothesis contradicts the starting point of the route in the premise
    label = "contradiction"
else:
    # if the starting point of the route in the hypothesis does not contradict the starting point of the route in the premise, we can infer entailment
    label = "entailment"

print(label)
