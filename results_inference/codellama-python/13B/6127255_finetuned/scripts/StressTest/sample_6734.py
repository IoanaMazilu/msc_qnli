start_road_premise = 2
start_avenue_premise = 3
end_road_premise = 10
end_avenue_premise = 5

start_road_hypothesis = 5
start_avenue_hypothesis = 3
end_road_hypothesis = 10
end_avenue_hypothesis = 5

# the hypothesis refers to the start and end points of Bill's walk, which are also mentioned in the premise
if start_road_hypothesis!= start_road_premise or start_avenue_hypothesis!= start_avenue_premise or end_road_hypothesis!= end_road_premise or end_avenue_hypothesis!= end_avenue_premise:
    # check if any of the start or end points in the hypothesis contradicts the ones in the premise
    label = "contradiction"
else:
    # if the start and end points in the hypothesis do not contradict the ones in the premise, we can infer entailment
    label = "entailment"

print(label)
