start_road_premise = 2
start_road_hypothesis = 5
start_ave_premise = 3
start_ave_hypothesis = 3

end_road_premise = 10
end_road_hypothesis = 10
end_ave_premise = 5
end_ave_hypothesis = 5

# the hypothesis talks about the starting point and destination of Bill's walk, referenced also in the premise
if start_road_premise!= start_road_hypothesis:
    # check if the starting road in the hypothesis contradicts the starting road in the premise
    label = "contradiction"
elif start_ave_premise!= start_ave_hypothesis:
    # check if the starting avenue in the hypothesis contradicts the starting avenue in the premise
    label = "contradiction"
elif end_road_premise!= end_road_hypothesis:
    # check if the destination road in the hypothesis contradicts the destination road in the premise
    label = "contradiction"
elif end_ave_premise!= end_ave_hypothesis:
    # check if the destination avenue in the hypothesis contradicts the destination avenue in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
