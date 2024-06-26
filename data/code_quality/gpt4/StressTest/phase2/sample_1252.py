start_road_premise = 1
start_road_hypothesis = 2
start_ave_premise = 3
start_ave_hypothesis = 3
end_road_premise = 7
end_road_hypothesis = 7
end_ave_premise = 8
end_ave_hypothesis = 8

# The hypothesis talks about the starting point and destination of Bill's walk, which are also mentioned in the premise
if start_road_hypothesis > start_road_premise:
    # If the starting road in the premise is less than the starting road in the hypothesis, 
    # it means that the starting point in the hypothesis is further than the one in the premise. 
    # Therefore, we cannot explicitly entail the hypothesis from the premise and it's a neutral case.
    label = "neutral"
elif start_ave_hypothesis != start_ave_premise or end_road_hypothesis != end_road_premise or end_ave_hypothesis != end_ave_premise:
    # If any of the other locations (starting avenue or destination) in the hypothesis contradicts 
    # the respective locations in the premise, it's a contradiction.
    label = "contradiction"
else:
    # If all locations in the hypothesis match the ones in the premise, then the hypothesis can be entailed from the premise.
    label = "entailment"

print(label)
