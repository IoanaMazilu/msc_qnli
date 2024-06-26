start_road_premise = 7
start_road_hypothesis = 2
start_ave_premise = 3
start_ave_hypothesis = 3
end_road_premise = 9
end_road_hypothesis = 9
end_ave_premise = 6
end_ave_hypothesis = 6

# the hypothesis refers to the starting and ending points of Bill's route mentioned in the premise
if start_road_hypothesis >= start_road_premise:
    # check if the starting road in the hypothesis contradicts the estimate of less than 'start_road_premise'
    label = "contradiction"
elif start_ave_hypothesis != start_ave_premise or end_road_hypothesis != end_road_premise or end_ave_hypothesis != end_ave_premise:
    # check if the starting avenue, ending road or ending avenue in the hypothesis contradicts the ones mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones and the starting road is less than 'start_road_premise', we can infer entailment
    label = "entailment"

print(label)
