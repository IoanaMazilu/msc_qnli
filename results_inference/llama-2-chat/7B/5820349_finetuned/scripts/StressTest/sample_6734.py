start_road_premise = 2
start_road_hypothesis = 5

# the hypothesis refers to the starting point of Bill's walk mentioned in the premise
if start_road_premise!= start_road_hypothesis:
    # check if the starting point in the hypothesis contradicts the starting point reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
