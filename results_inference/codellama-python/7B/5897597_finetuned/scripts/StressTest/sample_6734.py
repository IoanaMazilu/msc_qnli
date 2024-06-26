start_road_premise = 2
start_road_hypothesis = 5

# the hypothesis refers to the starting point of Bill's walk, which is also mentioned in the premise
if start_road_hypothesis!= start_road_premise:
    # check if the starting road in the hypothesis contradicts the starting road in the premise
    label = "contradiction"
else:
    # if the starting road in the hypothesis does not contradict the starting road in the premise, we can infer entailment
    label = "entailment"

print(label)
