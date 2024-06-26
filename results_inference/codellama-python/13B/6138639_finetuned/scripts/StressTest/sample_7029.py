start_road_premise = 2
start_avenue_premise = 3
end_road_premise = 9
end_avenue_premise = 6

start_road_hypothesis = 7
start_avenue_hypothesis = 3
end_road_hypothesis = 9
end_avenue_hypothesis = 6

# the hypothesis refers to the starting and ending points of the walk mentioned in the premise
if start_road_hypothesis <= start_road_premise:
    # check if the estimate of'start_road_hypothesis' contradicts the starting road in the premise
    label = "contradiction"
elif start_avenue_hypothesis!= start_avenue_premise:
    # check if the starting avenue in the hypothesis contradicts the starting avenue reported in the premise
    label = "contradiction"
elif end_road_hypothesis!= end_road_premise:
    # check if the ending road in the hypothesis contradicts the ending road reported in the premise
    label = "contradiction"
elif end_avenue_hypothesis!= end_avenue_premise:
    # check if the ending avenue in the hypothesis contradicts the ending avenue reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
