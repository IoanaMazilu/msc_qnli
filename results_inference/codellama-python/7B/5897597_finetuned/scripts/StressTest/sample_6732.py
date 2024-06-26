start_road_premise = 2
start_road_hypothesis = 3

# the hypothesis refers to the starting point of Bill's walk, also mentioned in the premise
if start_road_hypothesis <= start_road_premise:
    # check if the hypothesis value contradicts the starting point in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
