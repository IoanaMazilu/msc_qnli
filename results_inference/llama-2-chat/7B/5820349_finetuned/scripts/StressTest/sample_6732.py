start_road_premise = 2
start_road_hypothesis = 3

# the hypothesis refers to the starting point of Bill's journey mentioned in the premise
if start_road_hypothesis <= start_road_premise:
    # check if the estimate of'start_road_hypothesis' contradicts the starting point in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
